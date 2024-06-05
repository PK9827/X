import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Path to the PDF file in the same directory
pdf_path = 'test.pdf'

# Print the current working directory
print(f"Current working directory: {os.getcwd()}")

# Print the full path to the file
full_path = os.path.join(os.getcwd(), pdf_path)
print(f"Full path to the PDF: {full_path}")

# Check if the file exists
if os.path.exists(pdf_path):
    print(extract_text_from_pdf(pdf_path))
else:
    print(f"File not found: {pdf_path}")
