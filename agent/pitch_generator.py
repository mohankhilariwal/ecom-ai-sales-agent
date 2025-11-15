from jinja2 import Template
from utils.pdf_generator import html_to_pdf
import pandas as pd
def generate_pitch_deck(target_market: str, top_products: list):
    template = Template(open("templates/pitch_template.j2").read())
    html = template.render(
    target_market=target_market,
    products=top_products,
    author="Mohan Khilariwal",
    patent="US 12,540,924"
    )
    pdf_path = "output/pitch_deck.pdf"
    html_to_pdf(html, pdf_path)
    return pdf_path