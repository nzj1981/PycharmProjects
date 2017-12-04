import PyPDF2
# Put a watermark on all the original pdf files

with open('技术规范书.pdf', 'rb') as pdfFile:
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    totalPage = pdfReader.numPages
    pdfWriter = PyPDF2.PdfFileWriter()

    for pageNum in range(2):
        markObj = open('watermark.pdf', 'rb')
        warkMarkPage = PyPDF2.PdfFileReader(markObj).getPage(0)
        warkMarkPage.mergePage(pdfReader.getPage(pageNum))
        pdfWriter.addPage(warkMarkPage)
        newPdfObj = open('allwaterMarkPDF.pdf', 'wb')
        pdfWriter.write(newPdfObj)
        markObj.close()
        newPdfObj.close()
