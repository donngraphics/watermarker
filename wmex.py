import PyPDF2

input_file = 'super.pdf'
watermark_file = 'wtr.pdf'
output_file = 'superWM.pdf'

with open(input_file, 'rb') as inputfile:
    pdf = PyPDF2.PdfFileReader(inputfile)
    with open(watermark_file, 'rb') as watermarkfile:
        watermark = PyPDF2.PdfFileReader(watermarkfile)

        page1 = pdf.getPage(0)
        page2 = pdf.getPage(1)
        page3 = pdf.getPage(2)
        page4 = pdf.getPage(3)
        page1wm = watermark.getPage(0)

        page1.mergePage(page1wm)
        page2.mergePage(page1wm)
        page3.mergePage(page1wm)
        page4.mergePage(page1wm)

        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(page1)
        pdf_writer.addPage(page2)
        pdf_writer.addPage(page3)
        pdf_writer.addPage(page4)

        with open(output_file, 'wb') as outputfile:
            pdf_writer.write(outputfile)

            print('Finished!')
