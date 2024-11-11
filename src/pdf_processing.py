import fitz

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        # Open the PDF file
        with fitz.open(pdf_path) as pdf:
            # Loop through each page and extract text
            for page in pdf:
                text += page.get_text()
        return text
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return ""