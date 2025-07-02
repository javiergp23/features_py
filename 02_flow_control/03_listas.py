#listas

lista1 = [1, 2, 3, 4, 5]
lista2 = ["uno", "dos", "tres", "cuatro", "cinco"]
lista3 = [True, False, True, False, True]

#lista vacia
lista4 = []

#concatenar listas
lista5 = lista1 + lista2

#concatenar listas y convertir a string
lista6 = lista1 + lista2 + lista3

#concatenar listas y convertir a string
lista7 = lista1 + lista2 + lista3 + lista4

#concatenar listas y convertir a string
lista8 = lista1 + lista2 + lista3 + lista4 + lista5

print(lista5)

#acceder a elementos

print(lista2[-2])

#slicing de listas________________________

print(lista1[1:4])
#primers indices
print(lista1[:3])
# ultimos indices
print(lista1[3:])
#copia de la lista
print(lista1[:])

#lista saltando entren indices 
print(lista1[::2])
print(lista1[::-2]) #revertido

#añadir elementos a una lista
#forma larga
lista1 = lista1 + [6]
print(lista1)

#forma corta
lista1 += [7]
print(lista1)

#lingitud de la lista
print(len(lista1))

