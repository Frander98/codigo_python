#Programa sencillo para determinar si una palabra o frase en palíndromo o no.
palabra = input("Escribe una palabra: ")
palabra = palabra.lower()
palabra = palabra.replace(" ", "")

if palabra == palabra[::-1]:
  print("Verdadero, Es palíndromo")
else:
  print("Falso, No es palíndromo")