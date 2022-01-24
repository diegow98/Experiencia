import glob
import sys
import os

intervalos=list()

arg=sys.argv
txt=str(arg[1])
intervalos.append(int(arg[2]))
intervalos.append(int(arg[3]))

txt_divided=list()
for i in txt:
	txt_divided.append(i)



maximos=list()

for n in range(intervalos[0]-1, intervalos[1]+1):
	print(n)
	for file in sorted(glob.glob(str(n)+"_"+"*.txt")):
		with open(file , 'r') as f:
			coincidencias=0
			coincidencias_anteriores=0
			for line in f:
				index=0
				for letter in line:
					try:
						if letter == txt_divided[index]:
							coincidencias=coincidencias+1
					except:
						pass
					index=index+1
				if coincidencias>coincidencias_anteriores:
					coincidencias_anteriores=coincidencias
				coincidencias=0

		print('El maximo numero de coincidencias de %s fue realizado!' % file)
		maximos.append(str(coincidencias_anteriores))


if not os.path.exists('Resultados'):
	os.makedirs('Resultados')

with open('Resultados\\'+txt+' '+str(intervalos[0])+'-'+str(intervalos[1])+'.txt', 'w') as fd:
	for maximo in maximos:
		fd.write(maximo)
		fd.write("\n")








