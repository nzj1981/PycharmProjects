import PyPDF2

# get PDF number pages
with open('Go语言编程系列New.pdf', 'rb') as pdfFileObj:
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    numPages = pdfReader.numPages

    print('Now I know there are {} pages'.format(numPages))

    # reader PDF first page context
    pageObj = pdfReader.getPage(1)
    # extractText是不获取不中文字符
    print(pageObj.extractText())
