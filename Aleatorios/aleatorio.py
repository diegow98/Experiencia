import random
import os



num_ini=int(input("Introduce el número inicial: "))

num_fin=int(input("Introduce el número final: "))

num_por_linea=int(input("Introduce la cantidad de números por línea: "))

num_lineas=int(input("Introduce la cantidad de líneas: "))

num_dif=int(input("Introduce el número mínimo de diferencia entre líneas: "))

num_seguidos=int(input("Introduce el número de seguido que debe haber por línea: "))

grupos_concec=int(input("Introduce el numero de grupos concecutivos: "))

ordenar=input("Desea ordenar de menor a mayor (s/n)? ")

no_inc=input("Desea no incluir los numeors de (numeros_no_incluidos.txt) s/n?")

a=1
b=0

numYgrupos=num_seguidos*grupos_concec
line=[]

z=1
path=(str(z)+'_'+str(num_ini)+'-'+str(num_fin)+'-'+str(num_por_linea)+'-'+str(num_lineas)+'-'+str(num_dif)+'-'+str(num_seguidos)+'-'+str(grupos_concec)+'.txt')
while os.path.isfile(path) == True:
	z=z+1
	path=(str(z)+'_'+str(num_ini)+'-'+str(num_fin)+'-'+str(num_por_linea)+'-'+str(num_lineas)+'-'+str(num_dif)+'-'+str(num_seguidos)+'-'+str(grupos_concec)+'.txt')


linea=1

list1=[]
for i in range((num_por_linea-numYgrupos)):
	list1.append(i)

list2=[]
for i in range(num_por_linea):
	list2.append(i)
try:
	with open('numeros_no_incluidos.txt', 'r') as archivo:
		nros_no_ = [linea.split() for linea in archivo]
		nros_no=list()
		for i in nros_no_:
			nros_no=i
		nros_no = list(map(int, nros_no))
		archivo.close()
except:
	pass


dict1=dict()
salir=False
zz=0
with open(path, 'w') as f:
	while a<=num_lineas:
		if len(line) <num_por_linea:
			
			num= random.randint(num_ini, num_fin)

			w=random.choice(list2)

			if (w in list1):
				line.append(num)
				list2.remove(w)

			else:

				n=1
				for i in range(num_seguidos):
					line.append(num+n)
					n=n+1

				list2.remove(w)
				m=len(list2)
				while len(list2)!=(m-num_seguidos+1):
					g=random.choice(list2)
					if g not in list1:
						list2.remove(g)

		else:

			if zz!=0:
				salir=False
				repetido=False
				for j in line:
					if (line.count(j) >1):
						repetido=True
						break
					if no_inc=="s":
						if j in nros_no:
							repetido=True
							break

				if repetido==True:
					salir=True
					line=[]
					list2=[]
					for i in range(num_por_linea):
						list2.append(i)
					list1=[]
					for i in range((num_por_linea-numYgrupos)):
						list1.append(i)
				else:
					for i in dict1.values():
						fn=0
						for x in i:
							if x in line:
								fn=fn+1
							if fn>(num_por_linea-num_dif):
								salir=True
								line=[]
								list2=[]
								for i in range(num_por_linea):
									list2.append(i)
								list1=[]
								for i in range((num_por_linea-numYgrupos)):
									list1.append(i)
								break
						if salir:
							break
				if salir==False:

					if ordenar=="s":
						line.sort()

					for item in line:
						if line.index(item) == (len(line)-1):
							f.write("%s" % item)
						else:
							f.write("%s," % item)
					f.write("\n")
					dict1[linea]=line
					print("Se creo la línea: "+str(linea))
					linea=linea+1
					line=[]
					list2=[]
					for i in range(num_por_linea):
						list2.append(i)
					list1=[]
					for i in range((num_por_linea-numYgrupos)):
						list1.append(i)	
						
					a=a+1





			else:

				repetido=False
				for j in line:
					if line.count(j) >1:
						repetido=True
				if repetido==True:
					line=[]
					list2=[]
					for i in range(num_por_linea):
						list2.append(i)
					list1=[]
					for i in range((num_por_linea-numYgrupos)):
						list1.append(i)
				else:
					print(1)
					if ordenar=="s":
						line.sort()

					for item in line:
						if line.index(item) == (len(line)-1):
							f.write("%s" % item)
						else:
							f.write("%s," % item)
					f.write("\n")
					dict1[linea]=line
					print("Se creo la línea: "+str(linea))
					linea=linea+1
					line=[]
					list2=[]
					for i in range(num_por_linea):
						list2.append(i)
					list1=[]
					for i in range((num_por_linea-numYgrupos)):
						list1.append(i)	
					zz=zz+1
					a=a+1
