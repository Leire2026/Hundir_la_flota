import numpy as np
import random
BARCOS = [5]

def crear_tablero():
    return np.zeros((10, 10), dtype=int)
    

def colocar_barcos(tablero):
    for tamaño in BARCOS:
        colocado = False
        while not colocado:
            fila = random.randint(0, 9)
            col = random.randint(0, 9)
            orientacion = random.choice(['H', 'V'])

            if orientacion == 'H' and col + tamaño <= 9:
                if np.all(tablero[fila, col:col+tamaño] == 0):
                    tablero[fila, col:col+tamaño] = 1
                    colocado = True

            elif orientacion == 'V' and fila + tamaño <= 9:
                if np.all(tablero[fila:fila+tamaño, col] == 0):
                    tablero[fila:fila+tamaño, col] = 1
                    colocado = True


def mostrar_tablero(tablero, oculto=True):
    for fila in tablero:
        linea = ""
        for celda in fila:
            if oculto and celda == 1:
                linea += "~ "
            elif celda == 0:
                linea += "~ "
            elif celda == 1:
                linea += "B "
            elif celda == -1:
                linea += "O "
            elif celda == 2:
                linea += "X "
        print(linea)
    print()


def disparar(tablero, fila, col):
    if tablero[fila, col] == 1:
        tablero[fila, col] = 2
        return "Tocado"
    elif tablero[fila, col] == 0:
        tablero[fila, col] = -1
        return "Agua"
    else:
        return "Ya disparaste ahí"


def quedan_barcos(tablero):
    return np.any(tablero == 1)

def turno_jugador(tablero_maquina):
    while True:
        try:
            fila = int(input("Fila (0-9): "))
            col = int(input("Columna (0-9): "))
            resultado = disparar(tablero_maquina, fila, col)
            print(resultado)
            if resultado != "Ya disparaste ahí":
                break
        except:
            print("Entrada inválida")


def turno_maquina(tablero_jugador):
    while True:
        fila = random.randint(0, 9)
        col = random.randint(0, 9)
        if tablero_jugador[fila, col] in [0, 1]:
            resultado = disparar(tablero_jugador, fila, col)
            print(f"Máquina dispara a ({fila},{col}): {resultado}")
            break

def juego():
    jugador = crear_tablero()
    maquina = crear_tablero()

    colocar_barcos(jugador)
    colocar_barcos(maquina)

    while True:
        print("Tu tablero:")
        mostrar_tablero(jugador, oculto=False)

        print("Tablero enemigo:")
        mostrar_tablero(maquina, oculto=True)

        turno_jugador(maquina)
        if not quedan_barcos(maquina):
            print("¡Ganaste!")
            break

        turno_maquina(jugador)
        if not quedan_barcos(jugador):
            print("¡Perdiste!")
            break

