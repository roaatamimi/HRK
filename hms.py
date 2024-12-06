import pdfplumber

# Specify the path to your PDF file
pdf_file_path = "./katalog.pdf"  

# Create an empty string to store the extracted text
extracted_text = ""

# Open the PDF file
with pdfplumber.open(pdf_file_path) as pdf:
    # Loop through each page in the PDF
    for page in pdf.pages:
        # Extract text from the page and append it to the extracted_text string
        extracted_text += page.extract_text() + "\n"

# Save the extracted text to a file
with open("extracted_text.txt", "w", encoding="utf-8") as output_file:
    output_file.write(extracted_text)

print("Text extraction completed. Check 'extracted_text.txt' for the output.")