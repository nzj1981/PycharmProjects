#!/usr/bin/env python3.6
#coding=utf-8

import PyPDF2

# Pdf file plus password
with open('a.pdf', 'rb') as pdfFile:
    pdfReader = PyPDF2.PdfFileReader(pdfFile)

    pdfWriter = PyPDF2.PdfFileWriter()

    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    pdfWriter.encrypt('python')

    with open('encryptA.pdf', 'wb') as resultPdf:
        pdfWriter.write(resultPdf)