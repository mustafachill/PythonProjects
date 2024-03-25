from pdf2docx import Converter

pdf_path = ("samplee.pdf")
docx_path = "sample.docx"

converter = Converter(pdf_path)
converter.convert(docx_path)
converter.close()