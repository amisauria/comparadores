#FOR sirve para iterar una lista de elementos
#range ejecuta el numeros de veces hasta el mismo valor()-1  

buscar = 10
for numero in range(5):#es un iterable  
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encontre el numnero buscado :(")     

for char in "ultimate python":
    print(char) #pone cada letra del mensaje en vertical (?)



