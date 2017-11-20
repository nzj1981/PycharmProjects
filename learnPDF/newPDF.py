import PyPDF2

# pdf file name list
filenames = ['Go入门指南', 'Go语言编程', 'Go学习笔记第四版', 'GoWeb编程.v130123']
pdflist = []
# Traverse filenames save the pdf file as a new name
for filename in filenames:
    # new pdf file name append in pdflist
    pdflist.append(filename + 'New.pdf')
    # reader pdf file
    with open(filename + '.pdf', 'rb') as pdfBasicfile:
        pdfBasicReader = PyPDF2.PdfFileReader(pdfBasicfile)
        pdfWriter = PyPDF2.PdfFileWriter()

        # put the PDF file in memory and save i t to disk

        for pageNum in range(1, pdfBasicReader.numPages):
            pageObj = pdfBasicReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        # save the pdf file as a new name
        with open(filename + 'New.pdf', 'wb') as pdfOutputFile:
            pdfWriter.write(pdfOutputFile)
# save new pdf name of pdflist list
merger = PyPDF2.PdfFileMerger()

for pdfFile in pdflist:
    merger.append(PyPDF2.PdfFileReader(pdfFile))

merger.write('Go语言编程系列.pdf')