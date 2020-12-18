import PyPDF2
import os

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page1 = reader.getPage(0)
    # print(page1.rotateCounterClockwise(90))
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page1.rotateCounterClockwise(90))
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
