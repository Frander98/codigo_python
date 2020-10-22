colones = input("¿Cuántos colones costarricenses tienes?: ")
colones = float(colones)
dollar_value = 601.03
dollars_total = colones / dollar_value
dollars_total= round(dollars_total, 2) #Sirve para redondear a 2 decimales
dollars_total = str(dollars_total)
print("El equivalente en moneda USD " + "es de $" + dollars_total)
