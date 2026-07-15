import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    text = ""

    try:
        document = fitz.open(stream=pdf_file.read(), filetype="pdf")

        for page in document:
            text += page.get_text()

        document.close()

    except Exception as e:
        print("Error reading PDF:", e)

    return text