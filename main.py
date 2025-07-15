import copy

def imprimir_juego(juego):
    for i in range(0,3):
        for j in range(0,3):
            if j == 2:
                print(f" {juego[i][j]} ")
            else:
                print(f" {juego[i][j]} |", end="")
        if i != 2:
            print("-----------")

def jugador_tira(jugador):
    if jugador == 1:
        simbolo = "O"
    else:
        simbolo = "X"

    casilla = int(input("Ingresa la casilla donde quieres tirar (1-9): "))
    while casilla in casillas_ocupadas or casilla > 9 or casilla <= 0:
        print("Esa casilla no está disponible, intenta otra vez.")
        casilla = int(input("Ingresa la casilla donde quieres tirar (1-9): "))

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
        keep_playing = int(input("¿Deseas jugar otro juego? Ingresa 0 (No) o 1 (Sí): "))
        if keep_playing == 0:
            return False
        elif keep_playing == 1:
            return True
        else:
            print("Esa opción no es correcta. Escribe 0 o 1 únicamente.")



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

    for i in range(0,9):
        if i % 2 == 0:
            jugador_tira(1)
        else:
            jugador_tira(2)
        
        if i >= 4:
            if verificar_ganador():
                if i % 2 == 0:
                    print("¡El jugador 1 ha ganado!")
                else:
                    print("¡El jugador 2 ha ganado!")

                if not continuar_juego():
                    on = False
                break

            elif not verificar_ganador() and i == 8:
                print("Ha sido un empate.")
                if not continuar_juego():
                    on = False
                