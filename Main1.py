import PyPDF2
#from tkinter import Tk
import io
import glob
import pandas as pd
import xlsxwriter

word=input("Enter the word to search: ")
data=list()

for file in sorted(glob.glob("*.pdf")):
	try:
		pdfFileObject = open(file, 'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
		was_word=False
		words_quantity=0
		for page in range(pdfReader.numPages):
			pageObject = pdfReader.getPage(page)
			txt=pageObject.extractText()
			words_quantity=words_quantity+len(txt.split())
			print(txt.split())

			if word in txt:
				was_word=True
				text=txt
				text= text.replace("\n", "")

		if was_word:
			data_to_append=list()
			data_to_append.append(file)	
			data_to_append.append(words_quantity)
			data_to_append.append(word)
			data_to_append.append(text)
			data.append(data_to_append)
			del data_to_append

		if was_word==False:
			data_to_append=list()
			data_to_append.append(file)
			data_to_append.append(words_quantity)
			data_to_append.append(word)
			data_to_append.append('0')
			data.append(data_to_append)
			del data_to_append
		print(file+' COMPLETED')
	except:
		data_to_append=list()
		data_to_append.append(file)
		data_to_append.append("0")
		data_to_append.append(word)
		data_to_append.append('ERROR')
		data.append(data_to_append)
		del data_to_append				
		print(file+' COMPLETED')

df=pd.DataFrame(data,  columns=['ID','N°Words', 'Word', 'Text'])
writer = pd.ExcelWriter('Results.xlsx', engine='xlsxwriter')
df.to_excel("Results.xlsx", index=False)







