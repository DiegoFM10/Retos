def puntuarGanadores(punt1, punt2, secuenciaGanadores):
	cadenaGanadores = ""
	contador1 = 0
	contador2 = 0

	for ganador in secuenciaGanadores:
		for equipo1 in punt1:
			if (equipo1 in ganador):
					contador1 += 1
					break
		for equipo2 in punt2:
			if (equipo2 in ganador):
				contador2 += 1
				break
		if contador1 == contador2:
			cadenaGanadores = cadenaGanadores + 'L'
		elif contador1 > contador2:
			cadenaGanadores = cadenaGanadores + 'J'
		else:
			cadenaGanadores = cadenaGanadores + 'K'
		print(ganador + " - " + str(contador1) + " - "+ str(contador2) + " = "+ cadenaGanadores)

	return print(cadenaGanadores)

puntJugador1 = input('Ingresa puntaje jugador 1')
puntJugador2 = input('Ingresa puntaje jugador 2')
ganadores = input('Ingresa la secuencia de equipos ganadores')

puntuarGanadores(puntJugador1, puntJugador2, ganadores)


