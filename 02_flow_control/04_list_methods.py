#añadir un elemento a la lista

lista1 = [1, 2, 3, 4, 5]

#añadir al final de la lista
lista1.append(6)
print(lista1)


#insertar un elemento en cualquier posición
# se para primero el incide y luego el elemnto que se va a insertar luego de ese indice
lista1.insert(2, 7)
print(lista1)

#agregar varios elementos al final de la lista
lista1.extend(['ultimo', 'elemento'])
print(lista1)


#eliminar elemento de la lista # elimina el primer elemento que encuentra en coincidencia
lista1.remove('ultimo')
print(lista1)

#eliminar el ultimo de la lista #elimina el ultimo y lo devuelve
lista1.pop()
print(lista1)

#eliminar uso menos recomendado
del lista1[-1]
print(lista1)

#eliminar todos los elementos de la lista
lista1.clear()
print(lista1)

#ordenar listas_________________________________________
numbers = [8, 22,40, 55, 101, 135]

#ordenar lista modificando la lista
numbers.sort()
print(numbers)

#ordenar lista devolviendo una nueva lista
sorted_numbers = sorted(numbers)
print(sorted_numbers)