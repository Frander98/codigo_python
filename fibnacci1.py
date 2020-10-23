# Python 3: Fibonacci series up to n
#En la línea 8 "print(a, end=' ')" el "end=' '" significa que se imprima en la misma línea siempre que tenga espacio, si solo escribo un espacio en blanco me va a hacer un salto de línea cada vez que imprima un número.
#La sucesión de Fibonnacci incluye el 0.

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


fib(100)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

