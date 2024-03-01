import statistics

nombre = input("Por favor, introduce un nombre: ")
marca = []

with open('RCaverages.csv','r') as alumnos:
	for alumno in alumnos.readlines():
		alumno = alumno[0:-1]
		temp = alumno.split(",")
		if temp[0] == nombre:
			marca.append(float(temp[1]))

print(f'Las marcas para {nombre} son: ')

for i in range(len(marca)):
	print(marca[i])

# media = sum(marca)/len(marca)

print(f'La media de las marcas de {nombre} es {statistics.mean(marca)}')