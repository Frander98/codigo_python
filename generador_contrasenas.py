import random


def passwd_generator():
    cap_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'X', 'Y', 'Z']
    low_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbols = ['!', '#', '%', '$', '&', '/', '(', ')', '¡', '|', '?', '_', '<', '>']
    caracters = cap_letters + low_letters + simbols + numbers 
    pasword = []
    for item in range(25):
        caracter_random = random.choice(caracters)
        pasword.append(caracter_random)

    pasword = ''.join(pasword)
    return pasword



def run():
    password = passwd_generator()
    print("Tu nueva contraseña es " + password)


if __name__ == '__main__':
    run()