#Asks for a user name and prints de lenght of the name with a greeting

def run():
    name = input("Cuál es tu nombre: ")
    greeting = f'Hola {name}, espero que estés de maravilla'
    print(greeting)
    greeting = greeting.replace(' ', '')
    print(len(greeting))


if __name__ == '__main__':
    run()