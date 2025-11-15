from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from agent.rag_agent import build_rag_index

llm = ChatOllama(model="llama3.1:8b", temperature=0)

class SupportEngine:
    def __init__(self):
        self.rag_query_engine = build_rag_index()  # For catalog RAG
        # Load FAQs
        try:
            with open("data/faqs.txt", "r") as f:
                self.faqs = f.read()
        except FileNotFoundError:
            self.faqs = ""
        
        intent_prompt = PromptTemplate(
            input_variables=["query"],
            template="Classify intent: {query} (e.g., return, product_info, order_tracking)"
        )
        self.intent_chain = LLMChain(llm=llm, prompt=intent_prompt)

    def handle_query(self, query):
        intent = self.intent_chain.run(query)
        
        # Check FAQs first
        if "return" in query.lower() or "return" in intent.lower():
            if "return" in self.faqs.lower():
                return f"Intent: {intent}. FAQ Answer: 30 days for unworn items."
            rag_result = self.rag_query_engine.query("Return policy")
            return f"Intent: {intent}. {rag_result}"
        elif "track" in query.lower() or "order" in query.lower():
            if "track" in self.faqs.lower():
                return f"Intent: {intent}. FAQ Answer: Use order ID on our site."
            return f"Intent: {intent}. Please provide your order ID for tracking."
        else:
            # Use RAG for product queries
            rag_result = self.rag_query_engine.query(query)
            return f"Intent: {intent}. {rag_result}"