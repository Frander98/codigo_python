def conversor_mon_col_a_dol(tipo_mon):
  colones = float(input("Monto en " + tipo_mon))
  tasa_cambio = 600
  conversion = colones / tasa_cambio
  colones = round(colones, 2)
  conversion = round(conversion, 2)
  colones = str(colones)
  conversion = str(conversion)
  print("Conversión de " + colones + " colones a moneda USD es de $" + conversion)

def conversor_mon_dol_a_col(tipo_mon):
  dollars = float(input("Monto en " + tipo_mon))
  tasa_cambio = 600
  conversion = dollars * tasa_cambio
  dollars = round(dollars, 2)
  conversion = round(conversion, 2)
  dollars = str(dollars)
  conversion = str(conversion)
  print("Conversión de " + dollars + " dólares a moneda COL es de ¢" + conversion)

menu = """
Bienvenido al conversor de monedas 💲 😄
Elija la opción: 

1 es para convertir colones a dólares
2 es para convertir de dólares a colones 
 """

usr_option = input(menu)
usr_option = int(usr_option)

if usr_option == 1:
  conversor_mon_col_a_dol("colones ")
elif usr_option == 2:
  conversor_mon_dol_a_col("dólares ")
else:
  print("""
  Ingrese un valor válido a evaluar, por favor: 
  1 = COL => USD 
  2 = USD => COL
  """)
