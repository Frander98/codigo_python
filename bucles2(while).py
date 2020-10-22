#Programa para imprimir las potencias de 2 inferiores a LIMITE


def run():
    LIMITE = 1000
    exponente = 0
    potencia_de_2 = 2**exponente
    while potencia_de_2 < LIMITE:
      print("2 elevado a la " + str(exponente)+ " es igual a " + str(potencia_de_2))
      exponente += 1
      potencia_de_2 = 2**exponente
      
      
if __name__ == '__main__':
  run()