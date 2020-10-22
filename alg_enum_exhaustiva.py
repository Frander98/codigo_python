#Este es un ejemplo de un algortimo de enumeración exhaustiva en el que se evalúan todas las posibilidades hasta encontrar una respuesta. En este caso específico sirve para saber si {objetivo} tiene una raíz{respuesta} cuaadrada exacta o no. Lo que le decimos a la computadora es "Prueba todas las posibilidades hasta que la encuentres."

def run():
    objetivo = int(input("Escoge un número entero: "))
    respuesta = 0
    while respuesta ** 2 < objetivo:
        print(f'{respuesta} al cuadrado es {respuesta ** 2}')
        respuesta += 1
    if respuesta**2 == objetivo:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene raíz cuadrada exacta')

if __name__ == "__main__":
    run()
  