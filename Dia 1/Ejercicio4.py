#Ejercicio 4: Programa que encuentra el número mayor y menor de un conjunto de 10 numeros ingresados por el usuario

grande=0
pequeno=999999999999

for i in range(1,11):
    numerito=int(input("Ingresa el numero"))
    if grande==0 or pequeno==0:
        grande= numerito
        pequeno=numerito
    else:
        if numerito>grande:
            grande=numerito
        if numerito<pequeno:
            pequeno=numerito

print("Grande",grande)        
print("pequeño",pequeno)

## Desarrollado por: Sergio Rueda / T.I: 1.097.101.293


            
                 