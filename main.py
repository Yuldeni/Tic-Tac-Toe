import copy

def imprimir_juego(juego):
    '''Imprime el tablero del juego actualizado. '''
    print("\n")
    for i in range(0,3):
        for j in range(0,3):
            if j == 2:
                print(f" {juego[i][j]} ")
            else:
                print(f" {juego[i][j]} |", end="")
        if i != 2:
            print("-----------")
    print("\n")

def rellenar_tablero(casilla, simbolo):
    '''Ingresa el símbolo del jugador/IA en la posición correspondiente dentro del tablero.'''
    casillas_ocupadas.append(casilla)

    if casilla >= 1 and casilla <= 3:
        juego[0][casilla-1] = simbolo
    elif casilla >= 4 and casilla <= 6:
        juego[1][casilla-4] = simbolo
    elif casilla >= 7 and casilla <= 9:
        juego[2][casilla-7] = simbolo

def jugador_tira(num_jugador, nombre_jugador):
    '''Pregunta al jugador la casilla donde quiere tirar, y lo pasa a las funciones para actualizar el tablero.'''
    #El número de jugador indica el símbolo que le corresponde.
    if num_jugador == 1:
        simbolo = "O"
    else:
        simbolo = "X"

    casilla = int(input(f"{nombre_jugador}, ingresa la casilla donde quieres tirar (1-9): "))
    while casilla in casillas_ocupadas or casilla > 9 or casilla <= 0: #En caso de que se ingrese una casilla ocupada o menor/mayor al número posible.
        print("Esa casilla no está disponible, intenta otra vez.")
        casilla = int(input(f"{nombre_jugador}, ingresa la casilla donde quieres tirar (1-9): "))

    rellenar_tablero(casilla, simbolo)
    imprimir_juego(juego)

def ia_tira():
    '''Permite a la IA analizar el juego mediante pasos metódicos (intentar ganar -> evitar que el jugador gane -> tirar en posiciones estratégicas) 
    y tomar una decisión sobre donde tirar. Pasa la decisión a las funciones y actualiza el tablero.'''
    simbolo = "X"
    print("La IA está tirando...")

    #Primero, la IA busca una tirada con la que pueda ganar (2'X en misma fila/columna/diagonal)
    if not ia_tira_inteligente("X"):
        # print("La IA no ha encontrado una tirada con la que pueda ganar.")
        #Después, intenta tapar los intentos de ganar del otro jugador (2'Os en misma fila/columna/diagonal)
        if not ia_tira_inteligente("O"):
            # print("La IA ha intentado tapar, pero no hay necesidad.")

            #Si no es posible, busca tirar estratégicamente en las casillas restantes.
            casillas_buenas = [5, 1, 3, 7, 9] #Mejores casillas estratégicamente
            for element in casillas_buenas:
                if element not in casillas_ocupadas:
                    rellenar_tablero(element, simbolo)
                    si_tiro = 1
                    break

            if si_tiro != 1: #Tira en resto de casillas
                otras_casillas = [2, 4, 6, 8]
                for element in otras_casillas:
                    if element not in casillas_ocupadas:
                        rellenar_tablero(element, simbolo)
                        break

    imprimir_juego(juego)

def ia_tira_inteligente(simbolo):
    '''Permite a la IA analizar las filas y columnas para encontrar las que tengan 2 símbolos iguales (X o O), y terminar el juego o tapar según sea el caso.'''
    for i, row in enumerate(juego):
        if row.count(simbolo) == 2 and " " in row: #Detecta que hay 2X o 2O's en la misma línea y un espacio vacío
            for j, element in enumerate(row): #Enumera elementos de lista e índices
                if element == " ": #Rellena casilla vacía con X
                    juego[i][j] = "X"
            return True

    for i in range(0,3):
        lista_columna = []
        for j in range(0,3):
            lista_columna.append(juego[j][i])

        if lista_columna.count(simbolo) == 2 and " " in lista_columna:
            for k, element in enumerate(lista_columna):
                if element == " ":
                    juego[k][i] = "X"
            return True
    
    diag_der = [juego[i][i] for i in range(0,3)]
    if diag_der.count(simbolo) == 2 and " " in diag_der:
        for k, element in enumerate(diag_der):
            if element == " ":
                juego[k][k] = "X"
        return True

    diag_izq = [juego[0][2], juego[1][1], juego[2][0]]
    if diag_izq.count(simbolo) == 2 and " " in diag_izq:
        for k, element in enumerate(diag_izq):
            if element == " ":
                juego[k][2-k] = "X"
        return True
    
    return False #Si no se cumple ninguna condición no pudo ganar/tapar

def verificar_ganador():
    '''Analiza el juego y determina si hay una fila/columna/diagonal donde los 3 símbolos sean iguales, para declarar un ganador.'''
    #Realizamos una copia del juego, para tener casillas completamente vacías sin comprometer la estética del juego
    juego_temp = copy.deepcopy(juego)
    for i in range(0,3):
        for j in range(0,3):
            if juego[i][j] == " ":
                juego_temp[i][j] = ""

    booleanos = []
    # Compara si todos los elementos de la fila son iguales (al primero), y devuelve True. 
    # La función all devuelve True si todos los elementos son True.
    for row in juego_temp:
        if any(row): #Si hay un valor distinto a vacío ("") se hace el procedimiento. Esto evita True's por casillas vacías.
            booleanos.append(all(elemento == row[0] for elemento in row))

    # Compara si todos los elementos de cada columna son iguales.
    # Crea una lista de cada columna, y después compara si los elementos son iguales, y devuelve True si es así.
    # Repite el procedimiento en cada columna.    
    for i in range(0,3): #Recorre columnas
        lista_columna = []
        for j in range(0,3): #Recorre elementos de las columnas
            lista_columna.append(juego_temp[j][i])

        if any(lista_columna):
            booleanos.append(all(elemento == lista_columna[0] for elemento in lista_columna))

    # Compara si todos los elementos de la diagonal derecha son iguales
    diag_der = [juego_temp[i][i] for i in range(0,3)]
    if any(diag_der):
        booleanos.append(all(elemento == diag_der[0] for elemento in diag_der))

    # Compara si todos los elementos de la diagonal izquierda son iguales
    diag_izq = [juego_temp[0][2], juego_temp[1][1], juego_temp[2][0]]
    if any(diag_izq):
        booleanos.append(all(elemento == diag_izq[0] for elemento in diag_izq))

    return any(booleanos)

def continuar_juego():
    '''Permite al jugador tomar la decisión de volver a jugar o terminar el juego.'''
    keep_playing = -1
    while keep_playing != 0 or keep_playing != 1:
        keep_playing = int(input("\n¿Deseas jugar otro juego? Ingresa 0 (No) o 1 (Sí): "))
        if keep_playing == 0:
            print("¡Hasta luego!")
            return False
        elif keep_playing == 1:
            return True
        else: #Repite el ciclo hasta tener una decisión correcta
            print("Esa opción no es correcta. Escribe 0 o 1 únicamente.")

def pedir_jugadores():
    '''Acepta los nombres de los jugadores, y la decisión de jugar contra una IA si así se desea.'''
    jugador1 = input("Ingresa el nombre del jugador 1: ")

    ia_jugador = -1
    while ia_jugador != 1 and ia_jugador != 2:
        ia_jugador = int(input("¿Deseas jugar contra otro jugador (1), o contra una IA (2)? "))
        if ia_jugador == 1:
            jugador2 = input("Ingresa el nombre del jugador 2: ")
        elif ia_jugador == 2:
            jugador2 = "IA"
        else: #Repite el ciclo hasta tener una decisión correcta
            print("Esa opción no está disponible, inténtalo nuevamente")
    return jugador1, jugador2


on = True
print('''

░▒▓████████▓▒░▒▓█▓▒░░▒▓██████▓▒░       ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░       ░▒▓████████▓▒░▒▓██████▓▒░░▒▓████████▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░                ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░                ░▒▓█▓▒░  ░▒▓████████▓▒░▒▓█▓▒░                ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░   
   ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░                ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓██████▓▒░          ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░          ░▒▓█▓▒░   ░▒▓██████▓▒░░▒▓████████▓▒░ 
                                                                                                                                                                                                                                                   
''')

while on:
    #Bienvenida al juego y creación de variables iniciales
    print("Bienvenido a Tic Tac Toe!")
    juego = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
    casillas_ocupadas = []
    imprimir_juego(juego)
    jugador1, jugador2 = pedir_jugadores()

    #Crea ciclo de 9 tiros para Tic-Tac-Toe
    for i in range(0,9):
        if i % 2 == 0: #Si el tiro es par, tira jugador 1
            jugador_tira(1, jugador1)
        else: #Si el tiro es impar, tira jugador 2 o IA
            if jugador2 == "IA":
                ia_tira()
            else:
                jugador_tira(2, jugador2)
        
        #A partir del 5to tiro, se puede evaluar si alguien ha ganado. Antes no es posible.
        if i >= 4:
            if verificar_ganador(): #Si hay un ganador se anuncia
                if i % 2 == 0:
                    print(f"¡{jugador1} ha ganado!")
                else:
                    print(f"¡{jugador2} ha ganado!")

                if not continuar_juego(): #Si el jugador no desea jugar de nuevo, se rompe el ciclo.
                    on = False
                break

            elif not verificar_ganador() and i == 8: #Si no hubo ganador, y fue el último tiro, se anuncia el empate.
                print("Ha sido un empate.")
                if not continuar_juego():
                    on = False
                