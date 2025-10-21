# Importamos la librería random para la jugada aleatoria de la máquina
import random

# Creamos el tablero vacío, 9 posiciones vacías representadas por " "
tablero = [" "] * 9

# Función para mostrar el tablero de forma visual
def mostrar_tablero(tablero):
    print(tablero[0], "|", tablero[1], "|", tablero[2])
    print("--+---+--")
    print(tablero[3], "|", tablero[4], "|", tablero[5])
    print("--+---+--")
    print(tablero[6], "|", tablero[7], "|", tablero[8])

# Función para comprobar si hay ganador
def comprobar_ganador(tablero):
    # Todas las combinaciones posibles de victoria
    combinaciones = [
        [0,1,2], [3,4,5], [6,7,8],  # filas
        [0,3,6], [1,4,7], [2,5,8],  # columnas
        [0,4,8], [2,4,6]            # diagonales
    ]
    # Revisamos cada combinación
    for c in combinaciones:
        if tablero[c[0]] == tablero[c[1]] == tablero[c[2]] != " ":
            return tablero[c[0]]  # Devuelve "X" o "O" si alguien gana
    return None  # Si no hay ganador

#  elegir modo de juego antes de empezar
print("Bienvenido al 3 en raya 🎮")
print("Elige el modo de juego:")
print("1. Contra la máquina")
print("2. Contra otro jugador")

modo = input("Selecciona 1 o 2: ")
while modo not in ["1", "2"]:
    modo = input("Opción no válida. Elige 1 o 2: ")

# Bucle principal del juego
while True:
    mostrar_tablero(tablero)  # Mostramos el tablero antes de cada turno

    # ----- Turno del jugador -----
    while True:
        try:
            # Pedimos al jugador que elija una casilla del 0 al 8
            posicion = int(input("Elige una casilla (0-8): "))
            if posicion < 0 or posicion > 8:
                print("Número fuera de rango. Elige 0-8.")
                continue
            if tablero[posicion] == " ":  # Verificamos si está vacía
                tablero[posicion] = "X"   # Colocamos la X del jugador
                break  # Salimos del bucle del jugador
            else:
                print("Esa casilla ya está ocupada. Intenta otra.")
        except ValueError:
            print("Error: Debes introducir un número válido.")
        except (TypeError, IndexError) as e:
            print("Error de tipo o índice:", e)

    # Comprobamos si el jugador ha ganado
    ganador = comprobar_ganador(tablero)
    if ganador:
        mostrar_tablero(tablero)
        if ganador == "X":
            print("¡Has ganado!")
        else:
            print("La máquina ha ganado")
        break  # Fin del juego

    # Comprobamos si el tablero está lleno → empate
    if " " not in tablero:
        mostrar_tablero(tablero)
        print("¡Empate! No hay ganador.")
        break

    # ----- Turno del segundo jugador o la máquina -----
    if modo == "1":  # Contra la máquina
        posiciones_vacias = [i for i, valor in enumerate(tablero) if valor == " "]
        eleccion_maquina = random.choice(posiciones_vacias)
    else:  # Contra otra persona
        while True:
            try:
                posicion = int(input("Turno del jugador O (0-8): "))
                if posicion < 0 or posicion > 8:
                    print("Número fuera de rango. Elige 0-8.")
                    continue
                if tablero[posicion] == " ":
                    tablero[posicion] = "O"
                    break
                else:
                    print("Esa casilla ya está ocupada. Intenta otra.")
            except ValueError:
                print("Error: Debes introducir un número válido.")
            except (TypeError, IndexError) as e:
                print("Error de tipo o índice:", e)

                print("Esa casilla ya está ocupada. Intenta otra.")

    # Comprobamos si el segundo jugador o máquina ha ganado
    ganador = comprobar_ganador(tablero)
    if ganador:
        mostrar_tablero(tablero)
        if ganador == "X":
            print("¡Has ganado!")
        elif modo == "1":
            print("La máquina ha ganado")
        else:
            print("¡El jugador O ha ganado!")
        break

    # Comprobamos empate después del segundo turno
    if " " not in tablero:
        mostrar_tablero(tablero)
        print("¡Empate! No hay ganador.")
        break
