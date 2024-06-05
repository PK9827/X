import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def process_multiple_pdfs(pdf_paths):
    for pdf_path in pdf_paths:
        full_path = os.path.join(os.getcwd(), pdf_path)
        print(f"Processing file: {full_path}")
        if os.path.exists(pdf_path):
            print(extract_text_from_pdf(pdf_path))
        else:
            print(f"File not found: {pdf_path}")

# Get PDF files from user input
pdf_files = input("Enter the names of PDF files separated by commas: ").split(',')

# Strip any extra spaces from file names
pdf_files = [pdf_file.strip() for pdf_file in pdf_files]

# Print the current working directory
print(f"Current working directory: {os.getcwd()}")

# List files in the current directory
print(f"Files in current directory: {os.listdir(os.getcwd())}")

# Process each PDF file
process_multiple_pdfs(pdf_files)
