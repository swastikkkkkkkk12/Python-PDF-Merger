from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
n = int(input("How many pdf do you want to merge?: \n"))


for i in range(0,n):
    name = input(f"Enter the name of pdf{i + 1}:")
    pdfs.append(name)

for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()