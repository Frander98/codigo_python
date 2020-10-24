#Determina el área de un triángulo y determina el tipo de triángulo de acuerdo a los parámetros de la función

def run():
    base = float(input('Ingresa la base del triángulo: '))
    altura = float(input('Ingresa la altura del triángulo: '))
    area = (base * altura)/2
    print(f'El área del triángulo es {area}')


def clasificacion_triangulo(lado_1, lado_2, lado_3):
    if lado_1 == lado_2 == lado_3:
        print('Es un triángulo equilátero')
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print('Es un triángulo isósceles')
    else:
        print('Es un triángulo escaleno')



if __name__ == "__main__":
    run() 
    clasificacion_triangulo(100,10,80)