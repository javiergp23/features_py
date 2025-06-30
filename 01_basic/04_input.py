print('Hola como te llamas?')

nombre = input() # se puede pasar texto en el input pero queda en misma linea
# se puede agregar un escape \n para saltar la linea
print(f'Hola {nombre}')

#obtener varios valores en una entrada input

country, city = input("en que pais y ciudad vives?\n").split()

print(f"Hola vives en {country} y {city}")