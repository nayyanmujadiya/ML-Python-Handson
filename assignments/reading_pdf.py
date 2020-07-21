from tabula import read_pdf
import pandas as pd
import PyPDF2

#After you import Tika you need to initialize the Java Server
#Also, install full jdk - latest
import tika
tika.initVM()
from tika import parser

#option 1
parsedPDF = parser.from_file("CHINESE_TO_ENGLISH.pdf")
#parsedPDF = parser.from_file("Sample_document.pdf")
print(parsedPDF["metadata"])
print(parsedPDF["content"])

#option 2
# to read table
#df = read_pdf("Python_Basics.pdf")
#print(df)

#option 3
pdfFileObj = open('Sample_document.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
page1 = pageObj.extractText()
print(page1)

#after this you will have to do lots of string processing
