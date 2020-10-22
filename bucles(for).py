#Programa para imprimir las potencias de 2 empezando en 2**0 y  finalizando en 2**1000
 
def run():
    numbers = list(range(0, 1001))
    for n in numbers:
        print("2 elevado a la " + str(n) + " es igual a " + str(2**n))

if __name__ == '__main__':
    run()




      