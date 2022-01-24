import imagehash
from tkinter import *
from tkinter import filedialog
import os
import pandas as pd
from tkinter import messagebox

root=Tk()
root.title("Image Comparison")

folder_path=''
def folder_choose():
	global folder_path
	folder_path = filedialog.askdirectory()
	return folder_path

actual_file=1
data=list()
repeated=list()
def image_comparison():
	from PIL import Image
	global actual_file
	global data
	global repeated
	global folder_path

	img_hash=dict()

	for image in os.listdir(folder_path):
		try:
			img_hash[image]=imagehash.average_hash(Image.open(folder_path+'/'+image))
		except:
			pass
	for img in img_hash.keys():
		first_time=True
		if img not in repeated:
			for other_img in img_hash.keys():
				if other_img!=img:
					hash0 = img_hash[img]
					hash1 = img_hash[other_img]
					cutoff = 6.5
					if hash0 - hash1 < cutoff:
						repeated.append(other_img)
						if first_time==True:
							data_toAppend=list()
							data_toAppend.append(img)
							first_time=False
						data_toAppend.append(other_img)						


			if first_time:
				data_toAppend=list()
				data_toAppend.append(img)	
			try:

				data.append(data_toAppend)
				del data_toAppend
			except:
				pass

		n_files = len(os.listdir(folder_path))
		porcentage=((actual_file)*100)/n_files
		print(str(int(porcentage))+"%")
		actual_file=actual_file+1


	df=pd.DataFrame(data)
	df.to_excel("Similar_Images.xlsx", index=False)
	messagebox.showinfo("Image Comparison", "Finished!")
	root.destroy()


run_button= Button(root, text="Run", height = 5, width = 30, command=lambda:image_comparison())
run_button.grid(row=1, padx=4,pady=4, column=2)
folder_button= Button(root, text="Choose images folder", height = 5, width = 30, command=lambda:folder_choose())
folder_button.grid(row=1, padx=4,pady=4, column=1)






root.mainloop()