import random  # Importamos la librería para elegir cartas al azar

# Función para entregar una carta al jugador o a la máquina
def entregar_carta(mano):
    # Elegimos una carta al azar de la baraja
    # Los 10 repetidos representan J, Q, K; 11 es el As
    carta = random.choice([2,3,4,5,6,7,8,9,10,10,10,11])
    mano.append(carta)  # Añadimos la carta a la mano

# Función para calcular el total considerando los Ases
def total_mano(mano):
    total = 0
    ases = 0
    for carta in mano:
        if carta == 11:  # Si es As
            ases += 1
            total += 11  # Inicialmente contamos As como 11
        else:
            total += carta
    # Ajustar Ases: si nos pasamos de 21, cada As vale 1
    while total > 21 and ases > 0:
        total -= 10  # Cambiamos un As de 11 a 1
        ases -= 1
    return total

# Función para el turno de la máquina
def turno_maquina(mano_maquina):
    while total_mano(mano_maquina) < 17:
        entregar_carta(mano_maquina)
    print("Cartas de la máquina:", mano_maquina)
    print("Total máquina:", total_mano(mano_maquina))

# Función para determinar el ganador
def determinar_ganador(mano_jugador, mano_maquina):
    total_jugador = total_mano(mano_jugador)
    total_maquina = total_mano(mano_maquina)
    
    if total_jugador > 21 and total_maquina > 21:
        print("¡Ambos se pasaron! Gana la banca.")
    elif total_jugador > 21:
        print("Te pasaste. Gana la máquina.")
    elif total_maquina > 21:
        print("La máquina se pasó. ¡Has ganado!")
    elif total_jugador > total_maquina:
        print("¡Has ganado!")
    elif total_maquina > total_jugador:
        print("La máquina ha ganado.")
    else:
        print("¡Empate!")

# Bucle principal del juego
while True:
    mano_jugador = []
    mano_maquina = []
    
    # Repartimos 2 cartas iniciales
    entregar_carta(mano_jugador)
    entregar_carta(mano_jugador)
    entregar_carta(mano_maquina)
    entregar_carta(mano_maquina)
    
    # Turno del jugador
    while True:
        print("\nTus cartas:", mano_jugador)
        print("Total:", total_mano(mano_jugador))
        
        if total_mano(mano_jugador) > 21:
            print("¡Te pasaste!")
            break
        
        # Comentario: el jugador puede elegir otra carta
        respuesta = input("¿Quieres otra carta? (s/n): ")
        if respuesta.lower() == "s":
            entregar_carta(mano_jugador)
        else:
            print("Te plantas.")
            break
    
    # Turno de la máquina
    turno_maquina(mano_maquina)
    
    # Determinar ganador
    determinar_ganador(mano_jugador, mano_maquina)
    
    # Preguntar si quiere jugar otra vez
    respuesta = input("\n¿Quieres jugar otra vez? (s/n): ")
    if respuesta.lower() != "s":
        print("Gracias por jugar. ¡Hasta la próxima!")
        break
