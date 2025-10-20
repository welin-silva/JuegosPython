import random  # Librería para generar números aleatorios

# Generamos el número secreto del 1 al 10
numero_secreto = random.randint(1, 10)

# Número de intentos que tiene el jugador
intentos = 3

# Bucle principal: se repite mientras queden intentos
while intentos > 0:
    # Pedimos al usuario que escriba un número y lo convertimos a entero
    adivinanza = int(input("Adivina el número del 1 al 10: "))
    
    # Comprobamos si acertó
    if adivinanza == numero_secreto:
        print("¡Correcto! ¡Has adivinado el número!")
        break  # Salimos del bucle porque ganó
    # Si el número es menor que el secreto
    elif adivinanza < numero_secreto:
        print("El número es mayor.")
    # Si el número es mayor que el secreto
    else:
        print("El número es menor.")
    
    # Restamos un intento
    intentos -= 1
    print(f"Te quedan {intentos} intentos.\n")

# Si se acabaron los intentos y no acertó
if intentos == 0:
    print(f"Has perdido. El número era {numero_secreto}.")
