import glob
import numpy as np
from numba import njit, vectorize, jit


aciertos_1=14
aciertos_2=14
aciertos_3=13
aciertos_4=13
aciertos_5=0
aciertos_6=0
aciertos_7=0
aciertos_8=0
aciertos_9=0
aciertos_10=0
aciertos_11=0
aciertos_12=0
aciertos_13=0
aciertos_14=0
aciertos_15=0

lasquenosonde14=dict()

_14_aciertos=list()

if aciertos_1==14:
	_14_aciertos.append('aciertos_1')
else:
	lasquenosonde14['1']=aciertos_1
if aciertos_2==14:
	_14_aciertos.append('aciertos_2')
else:
	lasquenosonde14['2']=aciertos_2
if aciertos_3==14:
	_14_aciertos.append('aciertos_3')
else:
	lasquenosonde14['3']=aciertos_3
if aciertos_4==14:
	_14_aciertos.append('aciertos_4')
else:
	lasquenosonde14['4']=aciertos_4
if aciertos_5==14:
	_14_aciertos.append('aciertos_5')
else:
	lasquenosonde14['5']=aciertos_5
if aciertos_6==14:
	_14_aciertos.append('aciertos_6')
else:
	lasquenosonde14['6']=aciertos_6
if aciertos_7==14:
	_14_aciertos.append('aciertos_7')
else:
	lasquenosonde14['7']=aciertos_7
if aciertos_8==14:
	_14_aciertos.append('aciertos_8')
else:
	lasquenosonde14['8']=aciertos_8
if aciertos_9==14:
	_14_aciertos.append('aciertos_9')
else:
	lasquenosonde14['9']=aciertos_9
if aciertos_10==14:
	_14_aciertos.append('aciertos_10')
else:
	lasquenosonde14['10']=aciertos_10
if aciertos_11==14:
	_14_aciertos.append('aciertos_11')
else:
	lasquenosonde14['11']=aciertos_11
if aciertos_12==14:
	_14_aciertos.append('aciertos_12')
else:
	lasquenosonde14['12']=aciertos_12
if aciertos_13==14:
	_14_aciertos.append('aciertos_13')
else:
	lasquenosonde14['13']=aciertos_13
if aciertos_14==14:
	_14_aciertos.append('aciertos_14')
else:
	lasquenosonde14['14']=aciertos_14
if aciertos_15==14:
	_14_aciertos.append('aciertos_15')
else:
	lasquenosonde14['15']=aciertos_15	

num_decombinaciones={}

for archivo in glob.glob("*.txt"):

	if "aciertos_"+archivo[:-4] in _14_aciertos:
		count=0
		with open(archivo, 'r') as f:
			for line in f:
				count += 1
			num_decombinaciones[archivo]=count
		f.close()

base=min(num_decombinaciones, key=num_decombinaciones.get)

del num_decombinaciones[base]

with open(base,'r') as f:
	base=list()
	for line in f:
		line=line.replace('\n','')
		line = line[:-2]
		line=line.replace('X','3')
		base.append(line)


filtradas=set(base)

for archivo in num_decombinaciones.keys():
	temp_list=list()
	with open(archivo, 'r') as f:
		for line in f:
			line=line.replace('\n','')
			line = line[:-2]
			line=line.replace('X','3')
			temp_list.append(line)
		f.close()

	filtradas=filtradas.intersection(set(temp_list))

del base


filtradas=tuple(filtradas)

_13=list()
_12=list()
_11=list()
_10=list()
_9=list()
_8=list()
_7=list()
_6=list()
_5=list()
_4=list()
_3=list()
_2=list()
_1=list()
for value, key in lasquenosonde14.items():
	if key==13:
		_13.append(value)
	if key==12:
		_12.append(value)
	if key==11:
		_11.append(value)
	if key==10:
		_10.append(value)
	if key==9:
		_9.append(value)
	if key==8:
		_8.append(value)
	if key==7:
		_7.append(value)
	if key==6:
		_6.append(value)
	if key==5:
		_5.append(value)
	if key==4:
		_4.append(value)
	if key==3:
		_3.append(value)
	if key==2:
		_2.append(value)
	if key==1:
		_1.append(value)

del lasquenosonde14
t=0
def filtrar(_13global, filtradas, nroaciertos):
	global t
	if len(_13global)>0:
		_13=list()
		for archivo in _13global:
			_13a=list()
			with open(archivo+".txt", 'r') as f:
				for line in f:
					line=line.replace('\n','')
					line = line[:-2]
					line=line.replace('X','3')
					_13a.append(line)
			_13.append(_13a)
		del _13a
		iguales=filtradas
		_13_array=list()
		for n in _13:
			iguales=set(iguales).intersection(set(n))
			prov_array = np.array([np.array(list(x))for x in n])
			prov_array = prov_array.astype(np.int)
			_13_array.append(prov_array)
		filtradas=list(set(filtradas)-iguales)
		_13_array=np.array(_13_array)
		if t==0:	
			filtradas= np.array([np.array(list(x))for x in filtradas])
			filtradas= filtradas.astype(np.int)
			t=1
		else:
			filtradas=np.array(filtradas)

		
		#filtradas=filtradas[filtradas[:,1].argsort()]
		#_13_array=_13_array[_13_array[:,1].argsort()]
		
		#filtradas=np.array(sorted(filtradas,key=lambda x:x[0]))
		#_13_array=np.array(sorted(_13_array, key=lambda x:x[0]))
		#filtradas13=loop(_13_array, filtradas, nroaciertos)
		vfun=np.vectorize(loop, excluded=['_13_array', 'filtradas', 'nroaciertos'])
		filtradas13=vfun(_13_array=_13_array, filtradas=filtradas, nroaciertos=nroaciertos)
		filtradas13=list(filtradas13)
		iguales=list(np.array(list(x))for x in list(iguales))
		filtradas=filtradas13+iguales
		del filtradas13
		del _13

		return filtradas
	else:
		return filtradas

#np_arr = np.array(list(line))  # Convert to numpy array of characters

#np_arr_int = np_arr.astype(np.int)  # Convert each character to integer

@njit
def loop(_13_array, filtradas, nroaciertos):
	j=0
	q=0
	for i in range(len(filtradas)):
		c=0
		b=0
		for x in range(len(_13_array)):
			if b==0:
				for n in range(len(_13_array[x-1])):
					result = np.subtract(filtradas[i-1], _13_array[x-1, n-1])
					aciertos= np.count_nonzero(result == 0)
					b=b+1
					if aciertos>=nroaciertos:
						b=0
						c=c+1
						break
			else:
				break
		if c==len(_13_array):
			j=j+1
			print(j)
			if q==0:
				q=1				
				filtradas13=np.array([filtradas[i-1]])
			else:
				provarray=np.array([filtradas[i-1]])
				filtradas13=np.concatenate(filtradas13, provarray)



	return filtradas13
print('Empieza a comparar')
filtradas=filtrar(_13, filtradas, 13)
filtradas=filtrar(_12, filtradas, 12)
filtradas=filtrar(_11, filtradas, 11)
filtradas=filtrar(_10, filtradas, 10)
filtradas=filtrar(_9, filtradas, 9)
filtradas=filtrar(_8, filtradas, 8)
filtradas=filtrar(_7, filtradas, 7)
filtradas=filtrar(_6, filtradas, 6)
filtradas=filtrar(_5, filtradas, 5)
filtradas=filtrar(_4, filtradas, 4)
filtradas=filtrar(_3, filtradas, 3)
filtradas=filtrar(_2, filtradas, 2)
filtradas=filtrar(_1, filtradas, 1)

print('')
print('')
print(len(filtradas))

