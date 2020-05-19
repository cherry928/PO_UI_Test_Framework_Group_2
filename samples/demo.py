lista = [1,2,4,5,8]
for i in range(len(lista)):
	for j in range(0, len(lista)-1):
		if lista[j]<lista[j+1]:
			lista[j],lista[j+1] = lista[j+1], lista[j]

print(lista)
