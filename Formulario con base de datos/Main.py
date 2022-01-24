import sqlite3
from tkinter import *
from tkinter import messagebox

#Creamos la raiz y el frame principal. Agregamos titulo e icono a la ventana
raiz=Tk()
raiz.title("Diego SA")
raiz.iconbitmap("icono.ico")
raiz.resizable(width=False, height=False)

#Creamos todas las funciones que va a tener la app
	#primero el de los menus:
def crear_base():
	conex=sqlite3.connect("BBDD")
	cursor=conex.cursor()
	try:
		cursor.execute("CREATE TABLE USUARIOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR, CONTRASEÑA VARCHAR, APELLIDO VARCHAR, DIRECCION VARCHAR, COMENTARIOS VARCHAR)")
		messagebox.showinfo("BBDD", "La base de datos se ha creado correctamente")
	except:
		return messagebox.showwarning("BBDD", "La base de datos ya existe")
	
	conex.close()
	del conex
	del cursor

def salir():
	salirvar=messagebox.askokcancel("BBDD", "¿Esta seguro que quiere salir?")
	if salirvar==True:
		exit()

def borrar_campos():
	id_var.set("")
	nombre_var.set("")
	contraseña_var.set("")
	apellido_var.set("")
	direccion_var.set("")
	comentario_text.delete(1.0, END)

#Ahora creamos las de los botonoes y CRUD, que son las mismas

def create():
	global id_var
	global nombre_var
	global contraseña_var
	global direccion_var
	global apellido_var
	global comentario_text
	usuario=(nombre_var.get(), contraseña_var.get(), apellido_var.get(), direccion_var.get(), comentario_text.get(1.0, END))
	conect=sqlite3.connect("BBDD")
	cursor=conect.cursor()
	cursor.execute('INSERT INTO USUARIOS VALUES(NULL, ?, ?, ?, ?, ?)', usuario)
	conect.commit()
	conect.close()
	messagebox.showinfo("BBDD", "Registro añadido exitosamente")
	del usuario
	del conect
	del cursor

def leer():
	global id_var
	conect=sqlite3.connect("BBDD")
	cursor=conect.cursor()
	cursor.execute("SELECT NOMBRE, CONTRASEÑA, APELLIDO, DIRECCION, COMENTARIOS FROM USUARIOS WHERE ID='" + id_var.get() +"'")
	lectura=cursor.fetchall()
	for i in lectura:
		for j in i:
			if (i.index(j))==0:
				nombre_var.set(j)
			elif (i.index(j))==1:
				contraseña_var.set(j)
			elif (i.index(j))==2:
				apellido_var.set(j)
			elif (i.index(j))==3:
				direccion_var.set(j)
			else:
				comentario_text.delete(1.0, END)
				comentario_text.insert(1.0,j)
	conect.commit()
	conect.close()
	del conect
	del cursor
	del lectura

def actualizar():
	global id_var
	global nombre_var
	global contraseña_var
	global direccion_var
	global apellido_var
	global comentario_text
	conect=sqlite3.connect("BBDD")
	cursor=conect.cursor()
	cursor.execute("UPDATE USUARIOS SET NOMBRE='" + nombre_var.get() +
		"' ,CONTRASEÑA= '" + contraseña_var.get() +
		"' ,APELLIDO= '" + apellido_var.get() +
		"' ,DIRECCION= '" + direccion_var.get() +
		"' ,COMENTARIOS= '" + comentario_text.get(1.0, END) +"' WHERE ID='" + id_var.get() +"'")
	conect.commit()
	conect.close()
	messagebox.showinfo("BBDD", "Registro actualizado exitosamente")
	del conect
	del cursor

def borrar():
	global id_var
	conect=sqlite3.connect("BBDD")
	cursor=conect.cursor()
	cursor.execute("DELETE FROM USUARIOS WHERE ID='"+ id_var.get()+"'")
	conect.commit()
	conect.close()
	messagebox.showinfo("BBDD", "Registro borrado exitosamente")
	del cursor
	del conect


#Empezamos creando el menu principal, que es lo primero grafico que esta
menuPrincipal=Menu(raiz)
raiz.config(menu=menuPrincipal, width=300, height=150)

#Creamos el primer menu desplegable "BBDD"
bbdd_menu=Menu(menuPrincipal, tearoff=0)
menuPrincipal.add_cascade(label="BBDD", menu=bbdd_menu)
bbdd_menu.add_command(label="Conectar (crear)", command=lambda:crear_base())
bbdd_menu.add_command(label="Salir", command=lambda:salir())

#Ahora el de borrar
borrar_menu=Menu(menuPrincipal, tearoff=0)
menuPrincipal.add_cascade(label="Borrar", menu=borrar_menu)
borrar_menu.add_command(label="Borrar campos", command=lambda:borrar_campos())

#Ahora el de C.R.U.D
crud_menu=Menu(menuPrincipal, tearoff=0)
menuPrincipal.add_cascade(label="C.R.U.D", menu=crud_menu)
crud_menu.add_command(label="Crear", command=lambda:create())
crud_menu.add_command(label="Leer", command=lambda:leer())
crud_menu.add_command(label="Actualizar", command=lambda:actualizar())
crud_menu.add_command(label="Borrar", command=lambda:borrar())

#Ahora el de ayuda
ayuda_menu=Menu(menuPrincipal, tearoff=0)
menuPrincipal.add_cascade(label="Ayuda", menu=ayuda_menu)
ayuda_menu.add_command(label="Licencia")
ayuda_menu.add_command(label="Acerca de...")

#Ahora creamos el frame que va a contener el resto de la app
frame1=Frame(raiz)
frame1.pack()

#Ahora creamos todo lo que va en el frame1
id_label=Label(frame1, text="ID:")
id_label.grid(row=1, column=1, pady=2)
id_var=StringVar()
id_entry=Entry(frame1, textvariable=id_var)
id_entry.grid(row=1, column=2, pady=2)

nombre_label=Label(frame1, text="Nombre:")
nombre_label.grid(row=2,column=1, pady=2)
nombre_var=StringVar()
nombre_entry=Entry(frame1, textvariable=nombre_var)
nombre_entry.grid(row=2, column=2, pady=2)

contraseña_label=Label(frame1, text="Contraseña:")
contraseña_label.grid(row=3,column=1, pady=2)
contraseña_var=StringVar()
contraseña_entry=Entry(frame1, textvariable=contraseña_var)
contraseña_entry.grid(row=3, column=2, pady=2)
contraseña_entry.config(show="*")

apellido_label=Label(frame1, text="Apellido:")
apellido_label.grid(row=4,column=1, pady=2)
apellido_var=StringVar()
apellido_entry=Entry(frame1, textvariable=apellido_var)
apellido_entry.grid(row=4, column=2, pady=2)

direccion_label=Label(frame1, text="Dirección:")
direccion_label.grid(row=5,column=1, pady=2)
direccion_var=StringVar()
direccion_entry=Entry(frame1, textvariable=direccion_var)
direccion_entry.grid(row=5, column=2, pady=2)

comentario_label=Label(frame1, text="Comentarios:")
comentario_label.grid(row=6,column=1, pady=2)
comentario_text=Text(frame1, width=15, height=5)
comentario_text.grid(row=6, column=2, pady=2)
barraComentario=Scrollbar(frame1, command=comentario_text.yview)
barraComentario.grid(row=6, column=3, sticky="nsew")
comentario_text.config(yscrollcommand=barraComentario.set)

#Ahora creamos el frame2 y los botones que lleva
frame2=Frame(raiz)
frame2.pack()

crear_button=Button(frame2, text="Crear", width=8, command=lambda:create())
crear_button.grid(row=1, column=1, padx=2, pady=(10,4))

leer_button=Button(frame2, text="Leer", width=8, command=lambda:leer())
leer_button.grid(row=1, column=2, padx=2, pady=(10,4))

actualizar_button=Button(frame2, text="Actualizar", width=8, command=lambda:actualizar())
actualizar_button.grid(row=1, column=3, padx=2, pady=(10,4))

borrar_button=Button(frame2, text="Borrar", width=8, command=lambda:borrar())
borrar_button.grid(row=1, column=4, padx=2, pady=(10,4))



raiz.mainloop()