import PyPDF2
from docx import Document
import os
import re

def clean_text(text):
    # Remove leading/trailing whitespace and reduce multiple spaces to single space
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return clean_text(text)

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return clean_text('\n'.join(text))

def process_files(file_paths):
    for file_path in file_paths:
        full_path = os.path.join(os.getcwd(), file_path)
        print(f"Processing file: {full_path}")
        if os.path.exists(file_path):
            if file_path.lower().endswith('.pdf'):
                print(extract_text_from_pdf(file_path))
            elif file_path.lower().endswith('.docx'):
                print(extract_text_from_docx(file_path))
            else:
                print(f"Unsupported file type: {file_path}")
        else:
            print(f"File not found: {file_path}")

# Get files from user input
file_names = input("Enter the names of PDF or Word files separated by commas: ").split(',')

# Strip any extra spaces from file names
file_names = [file_name.strip() for file_name in file_names]

# Print the current working directory
print(f"Current working directory: {os.getcwd()}")

# List files in the current directory
print(f"Files in current directory: {os.listdir(os.getcwd())}")

# Process each file
process_files(file_names)
