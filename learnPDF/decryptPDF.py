#!D:\Python36\python3.exe
# coding=utf-8

import PyPDF2

# To pdf file decryption

with open('encryptA.pdf', 'rb') as pdfFileObj:
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    if pdfReader.isEncrypted:
        if pdfReader.decrypt('python'):
            pageObj = pdfReader.getPage(1)
            # extractText output pdf file context
            print(pageObj.extractText())
        else:
            print('Wrong password')
    else:
        pageObj = pdfReader.getPage(1)
        print(pageObj.extractText())


