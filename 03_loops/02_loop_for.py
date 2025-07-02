#ciclo for puede iterar sobre cualquier tipo de dato que sea iterable

frutas = ['manzana', 'pera', 'naranja', 'limon', 'mango']

for fruta in frutas:
    print(fruta)

nombre = "Javier"

for i in nombre:
    print(i)

#enumerate
for index, fruta in enumerate(frutas):
    print(f"El indice es: {index}, y la fruta es: {fruta}")

#for anidados
letras = ["a", "b", "c", "d", "e"]
numeros = [0, 1, 2, 3, 4]

for letra in letras:
    for numero in numeros:
        print(f"{letra} {numero}")