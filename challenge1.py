#Reto 1 - Clasificación de amigos
"""
Notas

4 categorías de amigos
	cUno = 0 - 20
	cDos = 21 - 30
	cTres = 31 - 50
	cCuatro = >50

Indice de calidad de amigos
	sumaAP = cantAmigos + cantPublicaciones
	indCalidadAmigo = sumaAP/5
    
cantPublicaciones = (cantAmigos - 4)/2
cantAmigos = (cantPublicaciones*2)-4
"""

def categoriaAmigo(indiceCalidad):

	#Condicional para evaluar la categoria del amigo
	if(indiceCalidad > 50):
		categoria = 'Cuatro'
	elif(indiceCalidad >= 31):
		categoria = 'Tres'
	elif(indiceCalidad >= 21):
		categoria = 'Dos'
	elif(indiceCalidad >= 0):
		categoria = 'Uno'
	else:
		categoria = 'Sin categoría'

	return categoria

def cantidadAmigos(cantPublicaciones):
	
	#Se calcula la cantidad de amigos con base en el número de publicaciones
	cantAmigos = (cantPublicaciones * 2) + 4
	return int(cantAmigos)

def indiceCalidadAmigos(cantPublicaciones):
	
	#Se calcula el indice de calidad de amigos teniendo en cuenta que: "la suma de la cantidad de amigos con la cantidad de publicaciones es igual a cinco veces el índice de calidad del amigo"
	sumaAmPubl = cantPublicaciones + cantidadAmigos(cantPublicaciones)
	indCalidadAmigo = sumaAmPubl / 5
	return int(indCalidadAmigo)

print("¡Bienvenido a UNtynder!, tu aplicación favorita para evaluar la calidad de tus amigos.")

#Solicitud del número de publicaciones del amigo a evaluar
numPublicaciones = int(input("Por favor ingresa la cantidad de publicaciones del amigo a evaluar:"))

#Uso de funciones para asignar la cantidad de amigos y el indice de calidad a unas variables
cantidadA = cantidadAmigos(numPublicaciones)
indCalAmigos = indiceCalidadAmigos(numPublicaciones)

#Impresión de resultados
print(numPublicaciones, end = " ")
print(cantidadA, end = " ")
print(indCalAmigos)
print(categoriaAmigo(indCalAmigos))