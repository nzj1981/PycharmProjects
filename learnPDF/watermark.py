import PyPDF2
# Add watermarks to the first page of the original pdf file
with open('watermark.pdf', 'rb') as markFile:
    pdfWaterReader = PyPDF2.PdfFileReader(markFile)
    waterMarkPage = pdfWaterReader.getPage(0)
    pdfWriter = PyPDF2.PdfFileWriter()

    with open('网络部署.pdf', 'rb') as pdfFile:
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        waterMarkPage.mergePage(pdfReader.getPage(0))
        pdfWriter.addPage(waterMarkPage)
        for pageNum in range(1, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        with open('waterMarkMinutes.pdf', 'wb') as resultPdfFile:
            pdfWriter.write(resultPdfFile)
