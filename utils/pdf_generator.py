from xhtml2pdf import pisa
import os
from io import BytesIO

def html_to_pdf(html_content, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Create PDF from HTML string
    with open(output_path, "w+b") as result_file:
        pisa_status = pisa.CreatePDF(
            html_content,
            dest=result_file,
            encoding='utf-8'
        )
    
    # Check if PDF was created successfully
    if pisa_status.err:
        raise Exception(f"Error creating PDF: {pisa_status.err}")
    
    return output_path