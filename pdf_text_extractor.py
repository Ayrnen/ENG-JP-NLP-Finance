import os
import pypdf

PATH = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = PATH + '/read/Japanese_Folk_Tales_ENG.pdf'

folk_in_eng = ''
with open(PDF_PATH, 'rb') as f:
    pdf_reader = pypdf.PdfReader(f)

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        folk_in_eng += text
        # print(f"Page {page_num + 1}:")

print(folk_in_eng[:200])