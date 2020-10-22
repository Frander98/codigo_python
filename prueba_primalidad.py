
def es_primo(numero):
    if numero < 2:
        return False
    elif numero == 2:
      return True
    else:
      for i in range(2, numero):
        if numero % i == 0:
          return False
        return True
      
    
def run():
  numero = int(input("Ingresa un número: "))
  if es_primo(numero) == True:
    print("Es primo")
  else:
    print("No es primo")
    

if __name__ == '__main__':
  run()