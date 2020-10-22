#Compares the value of two numbers, whether one is greater or equal than other.

username_1 = (input('¿Cuál es tu nombre? '))
userage_1 = int(input('¿Cuál es tu edad? '))
username_2 = (input('¿Cuál es tu nombre? '))
userage_2 = int(input('¿Cuál es tu edad? '))


def run():
    if userage_1 > userage_2:
        print(f'{username_1} es mayor que {username_2}')
    elif userage_1 < userage_2:
        print(f'{username_1} es menor que {username_2}')
    else:
        print(f'{username_1} es igual a {username_2}')


if __name__ == "__main__":
    run()