#sentencias condicionales
import os 
os.system("clear")

#condicional if

edad = 18

if edad >= 18:
    print("Eres mayor de edad")


#conficional if else

edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


#condicional elif

nota = 7

if nota >= 9:
    print("Sobresaliente!")
elif nota >= 7:
    print("Buena")
else:
    print("No esta calificado")

#operadores lógicos

edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Eres mayor de edad y tienes carnet🚗")
else:
    print("Eres menor de edad o no tienes carnet")

if edad >= 18 or tiene_carnet:
    print("Eres mayor de edad o tienes carnet🚗")
else:
    print("Eres menor de edad y no tienes carnet")


#negación lógica
fin_de_semana = False

if not fin_de_semana:
    print("No es fin de semana")