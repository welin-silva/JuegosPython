import random  # Importamos la librería para elegir la jugada de la máquina al azar

# Función para pedir la jugada del jugador
def eleccion_usuario(nombre):
    while True:
        jugada = input(f"{nombre}, elige piedra, papel o tijera: ").lower()
        if jugada in ["piedra", "papel", "tijera"]:
            return jugada  # Devuelve la jugada si es válida y termina la función
        else:
            print("Error: opción no válida. Intenta de nuevo.")  # Mensaje si la jugada no es válida

# Función para elegir al azar la jugada de la máquina
def eleccion_ordenador():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

# Función para decidir quién gana
def quien_gana(jugador, maquina):
    if jugador == maquina:
        return "Empate"
    elif (jugador == "piedra" and maquina == "tijera") or \
         (jugador == "papel" and maquina == "piedra") or \
         (jugador == "tijera" and maquina == "papel"):
        return "Jugador"
    else:
        return "Máquina"

# Función principal del juego
def juego():
    nombre = input("Escribe tu nombre: ")
    puntos_jugador = 0
    puntos_maquina = 0

    while puntos_jugador < 3 and puntos_maquina < 3:
        jugador = eleccion_usuario(nombre)
        maquina = eleccion_ordenador()
        print(f"La máquina eligió: {maquina}")

        ganador = quien_gana(jugador, maquina)

        if ganador == "Jugador":
            puntos_jugador += 1
            print(f"Gana {nombre} esta ronda")
        elif ganador == "Máquina":
            puntos_maquina += 1
            print("Gana la Máquina esta ronda")
        else:
            print("Empate esta ronda")

        print(f"Puntuación -> {nombre}: {puntos_jugador} | Máquina: {puntos_maquina}\n")

    # Mostrar quién ganó la partida
    if puntos_jugador == 3:
        print(f"¡{nombre} ganó la partida!")
    else:
        print("¡La Máquina ganó la partida!")

# Ejecutar el juego
juego()
