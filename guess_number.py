#Este es un pequeño "juego" en el que le pedimos al usuario que adivine un número aleatorio generado por la computadora. Este es un algoritmo de búsqueda binaria.
import random

def run():
  numero_aleatorio = random.randint(1, 100)
  numero_digitado = int(input("Escribe un número del 1 al 100: "))
  while numero_aleatorio != numero_digitado:
      if numero_digitado < numero_aleatorio:
          print("Escribe un número mayor ")
      else:
          print("Escribe un número menor")
      numero_digitado = int(input("Escribe otro número "))
  print("Felicidades, ganaste!")


if __name__ == '__main__':
  run()