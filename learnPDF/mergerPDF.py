import PyPDF2

# merger a.pdf, b.pdf to d.pdf

filenames = ['a.pdf', 'b.pdf']

merger = PyPDF2.PdfFileMerger()

for filename in filenames:
    merger.append(PyPDF2.PdfFileReader(filename))

merger.write('d.pdf')
