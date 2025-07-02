#funciones en python

def saludar():
    print("Hola")

saludar()

#con parametros

def saludar_a(nombre):
    print(f"Hola {nombre}")

saludar_a("Javier")

#documentar funciones con docstring
def suma(a, b):
    """suma dos numeros"""
    return a + b

print(suma(2, 3))

#parametros por defecto
def suma_con_parametros(a, b=5):
    return a + b
print(suma_con_parametros(2))