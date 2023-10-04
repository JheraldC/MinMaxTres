def printTablero(tablero):
    # Imprime el tablero en la pantalla
    print(tablero[1] + '|' + tablero[2] + '|' + tablero[3])
    print('-+-+-')
    print(tablero[4] + '|' + tablero[5] + '|' + tablero[6])
    print('-+-+-')
    print(tablero[7] + '|' + tablero[8] + '|' + tablero[9])
    print("\n")

def espacioDisponible(posicion):
    # Verifica si una posición en el tablero está disponible
    if tablero[posicion] == ' ':
        return True
    else:
        return False

def insertarLetra(letra, posicion):
    # Inserta una letra en la posición especificada en el tablero
    if espacioDisponible(posicion):
        tablero[posicion] = letra
        printTablero(tablero)
        if (comprobarEmpate()):
            print("¡Empate!")
            exit()
        if comprobarGanador():
            if letra == 'X':
                print("¡La computadora gana!")
                exit()
            else:
                print("¡El jugador gana!")
                exit()
    else:
        print("¡No se puede insertar ahí!")
        posicion = int(input("Por favor, ingrese una nueva posición: "))
        insertarLetra(letra, posicion)

def comprobarGanador():
    # Comprueba si hay un ganador
    if (tablero[1] == tablero[2] and tablero[1] == tablero[3] and tablero[1] != ' '):
        return True
    elif (tablero[4] == tablero[5] and tablero[4] == tablero[6] and tablero[4] != ' '):
        return True
    elif (tablero[7] == tablero[8] and tablero[7] == tablero[9] and tablero[7] != ' '):
        return True
    elif (tablero[1] == tablero[4] and tablero[1] == tablero[7] and tablero[1] != ' '):
        return True
    elif (tablero[2] == tablero[5] and tablero[2] == tablero[8] and tablero[2] != ' '):
        return True
    elif (tablero[3] == tablero[6] and tablero[3] == tablero[9] and tablero[3] != ' '):
        return True
    elif (tablero[1] == tablero[5] and tablero[1] == tablero[9] and tablero[1] != ' '):
        return True
    elif (tablero[7] == tablero[5] and tablero[7] == tablero[3] and tablero[7] != ' '):
        return True
    else:
        return False

def comprobarEmpate():
    # Comprueba si hay un empate
    for clave in tablero.keys():
        if (tablero[clave] == ' '):
            return False
    return True

def movimientoJugador():
    # Solicita al jugador su movimiento
    posicion = int(input("Ingrese la posición para 'O': "))
    insertarLetra(jugador, posicion)

def movimientoComputadora():
    # Implementación del movimiento de la computadora (IA)
    mejorPuntaje = -800
    mejorMovimiento = 0
    for clave in tablero.keys():
        if (tablero[clave] == ' '):
            tablero[clave] = computadora
            puntaje = minimax(tablero, 0, False)
            tablero[clave] = ' '
            if (puntaje > mejorPuntaje):
                mejorPuntaje = puntaje
                mejorMovimiento = clave
    insertarLetra(computadora, mejorMovimiento)

def minimax(tablero, profundidad, maximizando):
    # Implementación del algoritmo Minimax para la toma de decisiones de la computadora
    if (comprobarGanador(computadora)):
        return 1
    elif (comprobarGanador(jugador)):
        return -1
    elif (comprobarEmpate()):
        return 0

    if (maximizando):
        mejorPuntaje = -800
        for clave in tablero.keys():
            if (tablero[clave] == ' '):
                tablero[clave] = computadora
                puntaje = minimax(tablero, profundidad + 1, False)
                tablero[clave] = ' '
                if (puntaje > mejorPuntaje):
                    mejorPuntaje = puntaje
        return mejorPuntaje
    else:
        mejorPuntaje = 800
        for clave in tablero.keys():
            if (tablero[clave] == ' '):
                tab
