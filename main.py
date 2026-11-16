import PyPDF2

pdffiles = ["1.pdf", "2.pdf"]

merge = PyPDF2.PdfMerger()

for filename in pdffiles:
    with open(filename, "rb") as pdfFile:
        pdfReader = PyPDF2.PdfReader(pdfFile)
        merge.append(pdfReader)

merge.write("merged.pdf")
merge.close()

print("PDFs merged successfully!")