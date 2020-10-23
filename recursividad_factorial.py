def factorial(n):
    """n! = n * !(n-1)
    es decir, factorial de "n" es igual a factorial de "n-1",
    hay que definir un caso base para que no se haga un loop infinito
    cuando llegue a 0, 
    """
    print(n)
    if n == 0:
        return 1
    else: 
        return n * factorial(n-1)

print(factorial(6))
