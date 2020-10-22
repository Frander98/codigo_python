dollars = input("¿Cuántos dólares tienes?: ")
dollars = float(dollars)
tipo_cambio = 601.03
colones_total = dollars * tipo_cambio
colones_total = round(colones_total, 2)
colones_total = str(colones_total)
print("El equivalente en moneda COL es de ¢ " + colones_total)