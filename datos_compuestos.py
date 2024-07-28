# El primer tipo de dato compuesto que veremos sera la lista

lista = ["Camilo Velasquez Muñoz","tecnotutoriales Jheyson Galvis",True,1.74]
print(lista[1])
lista[3] ="mono"
print(lista[3])
# La tupla es una lista que no se puede modificar

tupla = ("Camilo Velasquez","tecnotutoriales Jheyson Galvis",True,1.74)
print(tupla[0])

#tupla[1]="tips TIC"
#print(tupla[1]) # No se puede modificar la tupla

# creando un conjunto o set

conjunto = {"Camilo Velasquez","tecnotutoriales Jheyson Galvis",True,1.74,1.74}

print(conjunto)

#creando un diccionario o map

diccionario ={
    "nombre":"Camilo",
    "apellidos":"Velasquez",
    "estatura":1.74,
    "esta feliz":True
    
}
print(diccionario["esta feliz"])
print(diccionario["nombre"])
print(diccionario["apellidos"])
print(diccionario["estatura"])