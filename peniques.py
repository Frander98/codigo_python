
def run():
    """Convierte del valor monetario del sistema monetario antiguo británico al sistema actual en valor de peniques"""

    print('Para el sistema monetario antiguo: ')
    user_libra = float(input('Escribe las libras: '))
    user_chelin = float(input('Escribe los chelines: '))
    user_penique = float(input('Escribe los peniques: '))
    valor_global_peniques = (user_libra*240) + (user_chelin*12) + (user_penique*1) 
    #Nuevo sistema (los chelines dejaron de existir)
    valor_global_peniques = (user_libra*100) + (user_penique*1)
    print('El valor en el sistema actual es de ' + str(valor_global_peniques) + ' peniques')


if __name__ == "__main__":
    run()