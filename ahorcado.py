from faker import Faker

#instalamos faker y lo descargamos

# Para instalar la librería faker desde la terminal, ejecuta:
# pip install faker

# Si estás usando Jupyter Notebook, puedes usar:
# !pip install faker

from faker import Faker
fake = Faker('Es_es')  # Configuramos Faker para usar datos en español
print(fake.word())  # Genera

def getPalabra(lista):
  palabra = random.choice(lista)
  return palabra

def getPalabraAleatoria():
  fake = Faker('ES-es')
  palabra = fake.word()
  return palabra

def transformaPalabra(palabra):
  estado = []
  for letra in palabra:
    estado.append('_')
  return estado

def reemplazarLetra(palabraSecreta, estado, letra):
  for n in range(0,len(palabraSecreta)):
    if letra == palabraSecreta[n]:
      estado[n] = letra
  return estado

def compruebaEstado(estado):
  if '_' not in estado:
    return True

def compruebaLetra(letra,palabraSecreta,estado,numIntentos):
  if letra in palabraSecreta:
    print('Has elegido una letra correcta')
    estado = reemplazarLetra(palabraSecreta, estado, letra)
  else:
    print('La letra no está en la palabra')
    numIntentos -= 1

  return estado, numIntentos

#codigo Principal
import random
from faker import Faker
listaPalabras = ['aurora','boreal','lobo','luna','jabali','cabra','queso']
aciertoFinal = False
numIntentos = 6
#opcion 2
palabraSecreta = getPalabra(listaPalabras)
estado = transformaPalabra(palabraSecreta)
#Truco para printar lista sin corchetes

while aciertoFinal == False and numIntentos > 0:
  print(" ".join(estado))
  #op2
  #print(*estado)
  letra = input('Introduzca una letra: ')
  estado, numIntentos = compruebaLetra(letra, palabraSecreta,estado, numIntentos)

  if compruebaEstado(estado):
    print('Has adivinado la palabra')
    aciertoFinal = True
  else:
    if numIntentos != 0:
      print(f'Te quedan {numIntentos} intentos')
    else:
      print('Game Over! No te quedan intentos')
