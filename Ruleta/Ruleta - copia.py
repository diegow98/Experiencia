from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
from io import open
from datetime import datetime
import pandas as pd
from tkinter import *
from tkinter import messagebox
import sqlite3
from pynput.mouse import Button as pynput_button
from pynput.mouse import Controller
from PIL import Image
from io import BytesIO
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

raiz=Tk()
raiz.title("Ruleta")
raiz.resizable(width=False, height=False)

def ocr_core(filename):
    text = pytesseract.image_to_string(filename)  
    return text


def leer(value):
	conect=sqlite3.connect("BD.db")
	cursor=conect.cursor()
	def menu():
		x=value
		return x

	cursor.execute("SELECT nombre, hora_ini, hora_fin, ult_num_bool FROM data WHERE nombre='" + menu() +"'")
	lectura=cursor.fetchall()
	for i in lectura:
		for j in i:
			if (i.index(j))==0:
				nombre_var.set(j)
			elif (i.index(j))==1:
				hora_ini.set(j)
			elif (i.index(j))==2:
				hora_fin.set(j)
			else:
				ult_num_bool.set(j)				
	conect.commit()
	conect.close()
	del cursor
	del conect
	del lectura

def guardar():

	config_=(hora_ini.get(), hora_fin.get(), ult_num_bool.get(), nombre_var.get())
	conect=sqlite3.connect("BD.db")
	cursor=conect.cursor()
	cursor.execute('INSERT INTO data VALUES(?, ?, ?, ?)', config_)
	conect.commit()
	conect.close()
	messagebox.showinfo("BD", "Registro añadido exitosamente")
	menu_loop()
	del config_
	del cursor
	del conect

def borrar():
	conect=sqlite3.connect("BD.db")
	cursor=conect.cursor()
	cursor.execute("DELETE FROM data WHERE nombre='"+ nombre_var.get()+"'")
	conect.commit()
	conect.close()
	messagebox.showinfo("BD", "Registro borrado exitosamente")
	configs_menu.delete(nombre_var.get())
	del cursor
	del conect

menuPrincipal=Menu(raiz)
raiz.config(menu=menuPrincipal, width=300, height=150)
configs_menu=Menu(menuPrincipal, tearoff=0)
menuPrincipal.add_cascade(label="Configuraciones", menu=configs_menu)

def menu_loop():
	value=nombre_var.get()
	configs_menu.add_command(label=value , command=lambda value=value:leer(value))
	del value

mi_conex=sqlite3.connect("BD.db")
cursor=mi_conex.cursor()
cursor.execute("SELECT nombre FROM data")
nombres=cursor.fetchall()
menus=list()
for j in nombres:
	for i in j:
		menus.append(i)

for value in menus:	
	configs_menu.add_command(label=value , command=lambda value=value:leer(value))	


frame1=Frame(raiz)
frame1.pack()

nombre_label=Label(frame1, text="Nombre:")
nombre_label.grid(row=1, column=1, pady=2)
nombre_var=StringVar()
nombre_entry=Entry(frame1, textvariable=nombre_var)
nombre_entry.grid(row=1, column=2, pady=2)

hora_ini_label=Label(frame1, text="Hora de inicio(HH:MM):")
hora_ini_label.grid(row=2,column=1, pady=2)
hora_ini=StringVar()
hora_ini_entry=Entry(frame1, textvariable=hora_ini)
hora_ini_entry.grid(row=2, column=2, pady=2)

hora_fin_label=Label(frame1, text="Hora de finalizacion(HH:MM):")
hora_fin_label.grid(row=3,column=1, pady=2)
hora_fin=StringVar()
hora_fin_entry=Entry(frame1, textvariable=hora_fin)
hora_fin_entry.grid(row=3, column=2, pady=2)

ult_num_bool_label=Label(frame1, text="Comenzar a guardar desde el ultimo numero? si/no:")
ult_num_bool_label.grid(row=4,column=1, pady=2)
ult_num_bool=StringVar()
ult_num_bool_entry=Entry(frame1, textvariable=ult_num_bool)
ult_num_bool_entry.grid(row=4, column=2, pady=2)

run_button=Button(frame1, text="Empezar", width=20, command=lambda:run())
run_button.grid(row=1, pady=2, column=3)
guardar_button=Button(frame1, text="Guardar", width=20, command=lambda:guardar())
guardar_button.grid(row=2, pady=2, column=3)
borrar_button=Button(frame1, text="Borrar", width=20, command=lambda:borrar())
borrar_button.grid(row=3, pady=2, column=3)

def change_proxy(proxy,port):
    profile = webdriver.FirefoxProfile();
    profile.set_preference("network.proxy.type", 1);
    profile.set_preference("network.proxy.http", proxy);
    profile.set_preference("network.proxy.http_port", port);
    profile.set_preference("network.proxy.ssl", proxy);
    profile.set_preference("network.proxy.ssl_port", port);
    driver = webdriver.Firefox(profile);
    return driver
	

def run():
	pag="https://www.merkurmagic.es/"
	user="Toribio95"
	passw="Ruleta88"
	boton_ini_xpath='/html/body/div[2]/div[4]/div[1]/div[4]/div[1]/div/div/div[2]/div[2]/button'
	input_user_xpath='/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[1]/div/input'
	input_contr_xpath='/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[2]/div/input'
	boton_submit_xpath='/html/body/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/form/div[2]'


	firefoxProfile = FirefoxProfile()
	firefoxProfile.set_preference("plugin.state.flash", 2)
	driver = webdriver.Firefox(firefoxProfile)
	driver.get(pag)
	time.sleep(5)
	boton_ini=driver.find_element_by_xpath(boton_ini_xpath)
	boton_ini.click()
	boton_user=driver.find_element_by_xpath(input_user_xpath)
	boton_user.send_keys(user)
	boton_contr=driver.find_element_by_xpath(input_contr_xpath)
	boton_contr.send_keys(passw)
	time.sleep(2)
	boton_submit=driver.find_element_by_xpath(boton_submit_xpath)
	boton_submit.click()
	time.sleep(5)
	'''mesas_deCasino=driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div[4]/div[2]/div/div/div[1]/ul/li[4]/a')
	mesas_deCasino.click()
	time.sleep(4)
	Ruleta3d= driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/div/div/div/div/div/div/div/div[2]/div/div[3]/div/div/div/ul/li[1]')
	Ruleta3d.click()'''
	driver.get('https://cachedownload.merkurmagic.es/casinoclient.html?game=ro3d&preferedmode=real&language=es&ngm=1#ro3d')
	time.sleep(6)
	mouse=Controller()
	time.sleep(1)
	mouse.position = (904, 272)
	time.sleep(1)
	mouse.press(pynput_button.left)
	mouse.release(pynput_button.left)


	#aceptar flash
	mouse.position = (402, 159)
	time.sleep(1)
	mouse.press(pynput_button.left)
	mouse.release(pynput_button.left)
	time.sleep(1)
	mouse.press(pynput_button.left)
	mouse.release(pynput_button.left)
	time.sleep(40)
	# cerrar msj
	mouse.position = (904, 272)
	time.sleep(1)
	mouse.press(pynput_button.left)
	mouse.release(pynput_button.left)
	#rojo
	time.sleep(1)	
	mouse.position = (644, 370)
	time.sleep(1)
	mouse.press(pynput_button.left)
	mouse.release(pynput_button.left)
	#negro
	time.sleep(1)	
	mouse.position = (724, 373)
	time.sleep(1)
	mouse.press(pynput_button.left)
	mouse.release(pynput_button.left)
	#girar
	time.sleep(1)
	mouse.position = (1023, 429)
	time.sleep(1)
	mouse.press(pynput_button.left)
	mouse.release(pynput_button.left)
	time.sleep(15)
	png = driver.get_screenshot_as_png()
	im = Image.open(BytesIO(png))
	left = 571
	top = 669
	right = 585
	bottom = 685
	im = im.crop((left, top, right, bottom))
	im.save('screenshot.png')
	img=Image.open("screenshot.png")
	num_ocr=ocr_core(img)
	img.show()
	print(num_ocr)

	#continuar
	time.sleep(1)	
	mouse.position = (737, 488)
	time.sleep(1)
	mouse.press(pynput_button.left)
	mouse.release(pynput_button.left)	
	#denuevo	
	mouse.position = (1015, 359)
	time.sleep(1)
	mouse.press(pynput_button.left)
	mouse.release(pynput_button.left)	




	
	"""
	ult_num=""
	if ult_num_bool.get()=="si":
		num_file=open("ult_num.txt", "r")
		ult_num=num_file.read()
		ult_num=str(ult_num)
		num_file.close()



	df=pd.read_excel("numeros.xls")
	agregar_nums=list()

	ult_num_passed=False

	while True:
		current_time = (datetime. now()).strftime("%H:%M")
		if hora_ini.get()==current_time:

			while ((datetime. now()).strftime("%H:%M")) != hora_fin:
				boton=driver.find_element_by_xpath(boton_xpath)
				boton.click()
				result=driver.find_element_by_xpath(result_xpath)
				result=result.text

				if (result==ult_num) or (ult_num_bool.get()=="no") or (ult_num_passed==True):
					agregar_nums.append(result)
					ult_num_passed=True

		if ((datetime. now()).strftime("%H:%M")) == hora_fin.get():
			break

	num_file=open("ult_num.txt", "w")
	num_file.seek(0)
	num_file.truncate()
	num_file.seek(0)
	num_file.write(result)
	num_file.close()

	cols=["num"]
	df2 = pd.DataFrame(agregar_nums, columns=cols)
	#df.append(df2, ignore_index=True, sort=False)
	new_df=pd.concat([df, df2], ignore_index=True, sort=False)
	print(new_df)
	new_df.to_excel("Numeros.xls", index=False)
	driver.close()

	exit()"""

	raiz.mainloop()

raiz.mainloop()