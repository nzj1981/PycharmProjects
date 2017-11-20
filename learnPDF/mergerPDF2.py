import PyPDF2

# merger a.pdf, b.pdf to d.pdf

filenames = ['Go入门指南New.pdf', 'Go语言编程New.pdf', 'Go学习笔记第四版New.pdf', 'GoWeb编程New.pdf']

merger = PyPDF2.PdfFileMerger()

for filename in filenames:
    merger.append(PyPDF2.PdfFileReader(filename))

merger.write('Go语言编程系列New.pdf')
