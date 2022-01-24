from math import sqrt
print("TEOREMA DE PITÁGORAS")
print()
print()


while 1==1:
	print()
	print()
	while True:
		try:	
			cat1=float(input("Introduce un cateto: "))
			cat2=float(input("Introduce el otro cateto: "))
			if cat1<0 or cat2<0:
				raise ValueError
			break
		except ValueError:
			print("Has introducido valores incorrectos. Vuelve a hacerlo")
			print()
	def Pitagoras(cate1, cate2):
		Hipotenusa=sqrt((cate1**2)+(cate2**2))
		return Hipotenusa

	print()
	print()

	print("La hipotenusa es:",Pitagoras(cat1, cat2) )
