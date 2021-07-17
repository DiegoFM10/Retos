def contadorCultivos(cultivos):
	listaContador = []
	cadenaCultivos = []
	contador = 0
	i = 0
	j = 0

	for cultivo in cultivos:
		
		if j < len(cultivos)-1:
			j += 1
		else:
			j = len(cultivos)-1
		if cultivo == cultivos[i]:
			contador += 1
			if cultivo != cultivos[j]:
				listaContador.append(contador)
				cadenaCultivos.append(cultivo)
				contador = 0
			elif i == len(cultivos)-1:
				listaContador.append(contador)
				cadenaCultivos.append(cultivo)
		elif contador == 0:
			i += 1
			contador = 0
		else:
			listaContador.append(contador)
			cadenaCultivos.append(cultivo)
			i += 1
			contador = 0	
		i += 1
					
	return print(cadenaCultivos), print(listaContador)

listaCultivos = input().split()
contadorCultivos(listaCultivos)