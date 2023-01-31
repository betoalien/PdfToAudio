#Importamos el módulo PyPDF2 para poder trabajar con archivos PDF
#We import the PyPDF2 module to be able to work with PDF files

import PyPDF2
from tkinter import filedialog

#Abrimos el archivo PDF que queremos convertir
#We open the PDF file we want to convert
filename = filedialog.askopenfilename(initialdir = "/", title = "Select A File", filetype = (("pdf files", "*.pdf"), ("all files", "*.*")))


pdfFileObj = open(filename, 'rb')

#Creamos un objeto lector PDF
#We create a PDF reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

#Contamos la cantidad de páginas del documento PDF
#We count the number of pages in the PDF document
numPages = len(pdfReader.pages)

#Creamos una cadena de texto con todo el contenido del documento
#We create a text string with all the content of the document
pdfText = ""

#Iteramos sobre cada una de las páginas del documento
#We iterate over each of the pages of the document
for page in range(0, numPages):
    #Extraemos el contenido de cada página
    #We extract the content of each page
    pageObj = pdfReader.pages[page]
    #Agregamos el contenido de cada página a la cadena de texto
    #We add the content of each page to the text string
    pdfText += pageObj.extract_text()

#Cerramos el archivo PDF
#We close the PDF file
pdfFileObj.close()

#Importamos el módulo gTTS para poder convertir una cadena de texto a audio
#We import the gTTS module to be able to convert a text string to audio
from gtts import gTTS

#Creamos el archivo de audio
#We create the audio file
audioFile = gTTS(text=pdfText, lang='es')

#Guardamos el archivo de audio
#We save the audio file
audioname = input("Ingrese el nombre del archivo de audio: ")
audioFile.save(audioname + ".mp3")