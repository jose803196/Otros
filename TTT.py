from collections import deque

#Creo un ciclo que varia entre dos valores para los simbolos
turno = deque(["0","X"])

#Creo el tablero de juego
tablero = [["","",""],["","",""],["","",""]]
tablero_numerico = [[10,10,10],[10,10,10],[10,10,10]]

def mostrar_tablero():
	"""Se encarga de mostrar el tablero cada vez que sea invocada la funcion"""
	print("")
	for fila in tablero:
		print (fila)

def mostrar_tableronumerico():
	"""Se encarga de mostrar el tablero cada vez que sea invocada la funcion"""
	print("")
	for fila in tablero_numerico:
		print (fila)

def r_turno():
	"""Se encarga de cambiar entre los dos simbolos del juego para cada jugador"""
	turno.rotate()
	return turno[0]

def verificacion_1(l_1, l_2):
	"""Se encarga de verificar que reciba un string con 2 valores y los retorna como lista"""
	f = l_1
	c = l_2
	return [int(f)-1, int(c)-1]

def verificacion_2(lugar_1):
	"""Se encarga de verificar que los parametros recibidos esten dentro del tablero del juego"""
	if (0 <= lugar_1[0] <= 2) and (0 <= lugar_1[1] <= 2):
		if tablero[lugar_1[0]][lugar_1[1]] == "":
			return True
	return False

def actualizar(lugar_1, jugador):
	"""Se encarga de marcar el simbolo en la posicion deseada por el usuario"""
	print(lugar_1)
	tablero[lugar_1[0]][lugar_1[1]] = jugador

def actualizar_numerico(lugar_1,jugador):
	"""Se encarga de marcar el numero en el tablero numerico"""
	if jugador == "X":
		tablero_numerico[lugar_1[0]][lugar_1[1]] = 1
	else:
		tablero_numerico[lugar_1[0]][lugar_1[1]] = 0


def ganador_numerico(j):
	"""Se encarga de comprobar su hay un ganador"""
	if sum(tablero_numerico[0]) == 3 or sum(tablero_numerico[1]) == 3 or sum(tablero_numerico[2]) == 3:
		return 3
	elif (int(tablero_numerico[0][0]) + int(tablero_numerico[1][0]) + int(tablero_numerico[2][0])) == 3:
		return 3
	elif (int(tablero_numerico[0][1]) + int(tablero_numerico[1][1]) + int(tablero_numerico[2][1])) == 3:
		return 3
	elif (int(tablero_numerico[0][2]) + int(tablero_numerico[1][2]) + int(tablero_numerico[2][2])) == 3:
		return 3	
	elif (int(tablero_numerico[0][0]) + int(tablero_numerico[1][1]) + int(tablero_numerico[2][2])) == 3:
		return 3
	elif (int(tablero_numerico[0][2]) + int(tablero_numerico[1][1]) + int(tablero_numerico[2][0])) == 3:
		return 3
	elif sum(tablero_numerico[0]) == 0 or sum(tablero_numerico[1]) == 0 or sum(tablero_numerico[2]) == 0:
		return 0
	elif (int(tablero_numerico[0][0]) + int(tablero_numerico[1][0]) + int(tablero_numerico[2][0])) == 0:
		return 0
	elif (int(tablero_numerico[0][1]) + int(tablero_numerico[1][1]) + int(tablero_numerico[2][1])) == 0:
		return 0
	elif (int(tablero_numerico[0][2]) + int(tablero_numerico[1][2]) + int(tablero_numerico[2][2])) == 0:
		return 0	
	elif (int(tablero_numerico[0][0]) + int(tablero_numerico[1][1]) + int(tablero_numerico[2][2])) == 0:
		return 0
	elif (int(tablero_numerico[0][2]) + int(tablero_numerico[1][1]) + int(tablero_numerico[2][0])) == 0:
		return 0
	else:
		False


 
def jugar():
	"""Esta es la funcion principal del programa ya que se encarga de simular el juego en cada aspecto."""
	while True:
		usuario = input("Eliga entre X o O: ")
		if (usuario == "X") or (usuario == "x") or (usuario == "O") or (usuario == "0") or (usuario == "o"):
			break
		else:
			pass

	mostrar_tablero()
	#mostrar_tableronumerico()
	jugador = r_turno()
	n = 1
	while True:
		l_1 = input("Turno de {}. Elige una fila: ".format(jugador))
		l_2 = input("Turno de {}. Elige una columna: ".format(jugador))
		if l_1 == 'salir' or l_2 == 'salir':
			break
		try:
			lugar_1 = verificacion_1(l_1, l_2)
		except:
			print("La posicion {},{} no es permitida.".format(l_1, l_2))
			continue
		if verificacion_2(lugar_1):
			#print("Correcta")
			actualizar(lugar_1, jugador)
			actualizar_numerico(lugar_1,jugador)
			mostrar_tablero()
			#mostrar_tableronumerico()
			if ganador_numerico(jugador) == 3:
				print("Jugador de X ha ganado.")
				break
			elif ganador_numerico(jugador) == 0:
				print("Jugador de 0 ha ganado.")
				break
			elif n == 9:
				print("El juego termino en empate.")
				break
			jugador = r_turno()
		else:
			print("La posicion {},{} es incorrecta.".format(l_1,l_2))
		n+=1

#Ejecuto la funcion jugar que corre el programa
TTT = jugar()