import copy

def imprimir_juego(juego):
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

def jugador_tira(num_jugador, nombre_jugador):
    if num_jugador == 1:
        simbolo = "O"
    else:
        simbolo = "X"

    casilla = int(input(f"{nombre_jugador}, ingresa la casilla donde quieres tirar (1-9): "))
    while casilla in casillas_ocupadas or casilla > 9 or casilla <= 0:
        print("Esa casilla no está disponible, intenta otra vez.")
        casilla = int(input(f"{nombre_jugador}, ingresa la casilla donde quieres tirar (1-9): "))

    casillas_ocupadas.append(casilla)

    if casilla >= 1 and casilla <= 3:
        juego[0][casilla-1] = simbolo
        imprimir_juego(juego)
    elif casilla >= 4 and casilla <= 6:
        juego[1][casilla-4] = simbolo
        imprimir_juego(juego)
    elif casilla >= 7 and casilla <= 9:
        juego[2][casilla-7] = simbolo
        imprimir_juego(juego)
    else:
        print("Esa opción no está disponible.")

def ia_tira():
    simbolo = "X"
    print("La IA está tirando...")
    if not ia_tira_inteligente("X"):
        print("La IA no ha encontrado una tirada con la que pueda ganar. Buscando tapar...")
        if not ia_tira_inteligente("O"):
            print("La IA ha intentado tapar, pero no hay necesidad.")

            casillas_buenas = [5, 1, 3, 7, 9]
            for element in casillas_buenas:
                if element not in casillas_ocupadas:
                    casillas_ocupadas.append(element)

                    if element >= 1 and element <= 3:
                        juego[0][element-1] = simbolo
                    elif element >= 4 and element <= 6:
                        juego[1][element-4] = simbolo
                    elif element >= 7 and element <= 9:
                        juego[2][element-7] = simbolo

                    si_tiro = 1
                    break

            if si_tiro != 1:
                otras_casillas = [2, 4, 6, 8]
                for element in otras_casillas:
                    if element not in casillas_ocupadas:
                        casillas_ocupadas.append(element)

                        if element >= 1 and element <= 3:
                            juego[0][element-1] = simbolo
                        elif element >= 4 and element <= 6:
                            juego[1][element-4] = simbolo
                        elif element >= 7 and element <= 9:
                            juego[2][element-7] = simbolo

                        break

    imprimir_juego(juego)
    

def ia_tira_inteligente(simbolo):
    for i, row in enumerate(juego):
        if row.count(simbolo) == 2 and " " in row: #Detecta que hay 2X's en la misma línea y un espacio vacío
            for j, element in enumerate(row): #Enumera elementos de lista e índices
                if element == " ":
                    juego[i][j] = "X"
            return True

    for i in range(0,3): #Recorre columnas
        lista_columna = []
        for j in range(0,3): #Recorre elementos de las columnas
            lista_columna.append(juego[j][i])

        if lista_columna.count(simbolo) == 2 and " " in lista_columna:
            for k, element in enumerate(lista_columna):
                if element == " ":
                    juego[k][i] = "X"
            return True
    
    diag_der = []
    for i in range(0,3): 
        diag_der.append(juego[i][i])
        
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
    
    return False



def verificar_ganador():
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
    diag_der = []
    for i in range(0,3): 
        diag_der.append(juego_temp[i][i])
    if any(diag_der):
        booleanos.append(all(elemento == diag_der[0] for elemento in diag_der))

    # Compara si todos los elementos de la diagonal izquierda son iguales
    diag_izq = [juego_temp[0][2], juego_temp[1][1], juego_temp[2][0]]
    if any(diag_izq):
        booleanos.append(all(elemento == diag_izq[0] for elemento in diag_izq))

    return any(booleanos)

def continuar_juego():
    keep_playing = -1
    while keep_playing != 0 or keep_playing != 1:
        keep_playing = int(input("\n¿Deseas jugar otro juego? Ingresa 0 (No) o 1 (Sí): "))
        if keep_playing == 0:
            print("¡Hasta luego!")
            return False
        elif keep_playing == 1:
            return True
        else:
            print("Esa opción no es correcta. Escribe 0 o 1 únicamente.")

def pedir_jugadores():
    jugador1 = input("Ingresa el nombre del jugador 1: ")

    ia_jugador = -1
    while ia_jugador != 1 and ia_jugador != 2:
        ia_jugador = int(input("¿Deseas jugar contra otro jugador (1), o contra una IA (2)? "))
        if ia_jugador == 1:
            jugador2 = input("Ingresa el nombre del jugador 2: ")
        elif ia_jugador == 2:
            jugador2 = "IA"
        else:
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
    print("Bienvenido a Tic Tac Toe!")
    juego = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
    casillas_ocupadas = []
    imprimir_juego(juego)
    jugador1, jugador2 = pedir_jugadores()

    for i in range(0,9):
        if i % 2 == 0:
            jugador_tira(1, jugador1)
        else:
            if jugador2 == "IA":
                ia_tira()
            else:
                jugador_tira(2, jugador2)
        
        if i >= 4:
            if verificar_ganador():
                if i % 2 == 0:
                    print(f"¡{jugador1} ha ganado!")
                else:
                    print(f"¡{jugador2} ha ganado!")

                if not continuar_juego():
                    on = False
                break

            elif not verificar_ganador() and i == 8:
                print("Ha sido un empate.")
                if not continuar_juego():
                    on = False
                