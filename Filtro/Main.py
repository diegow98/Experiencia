import glob
import os

archivos_de_14=list()


with open('archivos.txt', 'r') as f:
	for line in f:
		line=line.replace('\n','')
		archivos_de_14.append(line)
a=0

for archivo in archivos_de_14:
	temp_list=list()
	with open(archivo+'.txt', 'r') as f:
		for line in f:
			line=line.replace('\n','')
			line = line[:-2]
			temp_list.append(line)
		f.close()
	if a == 0:
		filtradas=temp_list
		a=1
	else:
		filtradas=set(filtradas).intersection(set(temp_list))

filtradas=tuple(filtradas)

repetido=1
path=str(repetido)+'_'+str(len(filtradas))+'filas'+'_'+ ''.join((str(x)+'_' for x in archivos_de_14))

while os.path.isfile(path) == True:
	z=z+1
	path=str(repetido)+'_'+str(len(filtradas))+'filas'+'_'+ ''.join((str(x)+'_' for x in archivos_de_14))

with open(path, 'w') as f:
	for combinacion in filtradas:
		f.write(combinacion)
		f.write('\n')

	file.close()