##Ejericio 7 - Filtro Python Sergio Rueda
##Numeros Amigos

##1er Paso - Pedir los dos numeros y tener dos variables que almacenen las dos sumatorias

num1=int(input("Ingresa el primer número:"))
num2=int(input("Ingresa el segundo número:"))

suma1=0
suma2=0

##2ndo - Crear los ciclos que busquen los divisores

for i in range(1,num1):
    if(num1%i==0):
        suma1=suma1+i
for i in range(1,num2):
    if(num2%i==0):
        suma2=suma2+i

##3er - Comparar si la sumatoria de A es igual al numero B y viceversa
if(suma1 == num2 and suma2==num1):
    print("Los numeros son bros!")
else:
    print("Los números no son bros :sadfeis:")

## Desarrollado por: Sergio Rueda / T.I: 1.097.101.293
