# tipado dinamico de variables
my_name = "javier"

print(my_name)

age = 32

print(age)


#tipado dinamico
#Tipado fuerte por que no convierte datos

print(f"Hola mi nombre es: {my_name}, y mi edad es {age +1}")

#forma no recomendada de asignar variables
name, edad, ciudad = "Eduardo", 32, "Santiago"

#convenciones de nombres variables
mi_nombre_es = "javier" #snake_case

nombre = "ok"

MiNombreEsJavier = "ok" #PascalCase

MI_CONSTANTE = 3.14

print(MI_CONSTANTE)

#Palabras reservadas
# False, None, True, and, as, assert
# async, await, break, class, continue,
# def, del, elif, else, except, finally,
# for, from, global, if, import, in,
# is, lambda, nonlocal, not, or, pass,
# raise, return, try, while, with, yield

#type anotation - comentario para saber que tipo es, pero en ejecución no se revisan los tipos
is_user_logger: bool = True