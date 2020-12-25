import PyPDF2
from PyPDF2 import PdfFileReader
import re

start_regex = r"([\d])\."
end_regex2 = r"(\. \d )"
end_regex1 = r"(\d\+\d)"
pdf = open("MPC-001 (1).PDF", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf)
num_pages = pdf_reader.numPages
page = pdf_reader.getPage(1)
str_text = page.extractText()
questionFound =""
while re.search(start_regex, str_text):
    start_match = re.search(start_regex, str_text)
    end_match = re.search(end_regex1, str_text)
    if not end_match:
        end_match = re.search(end_regex2, str_text)
    if end_match:
        questionFound = str_text[start_match.end():end_match.start()]
        print(questionFound)
    else:
        break;
    str_text = str_text[end_match.end():]
