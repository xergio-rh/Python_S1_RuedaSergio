##Ejercicio 7: Programa para determinar si dos numeros son amigos

n1=int(input("Ingresa el primer numero:"))
n2=int(input("Ingresa el segundo numero:"))

suma1=0
suma2=0

for i in range (1,n1):
    if (n1 % i==0):
        suma1=suma1 + i

for i in range (1,n2):
    if (n2 % i==0):
        suma2=suma2 + i

if (suma1==n2 and suma2==n1):
    print("son numeros amigos")
else:
    print("son numeros enemigos")


##Desarrollado por: Sergio Rueda / T.I: 1.097.101.293



##Ejericio 7 Pro- Filtro Python
##Numeros Amigos

def suma_divisores_propios(n):
    suma=0
    for i in range(1,n):
        if n%i == 0:
            suma += i #suma=suma+i
    return suma

def numeros_amigos(a,b):
    return suma_divisores_propios(a) == b and suma_divisores_propios(b) == a

num1=int(input("Ingresa el primer número:"))
num2=int(input("Ingresa el segundo número:"))

if(numeros_amigos(num1,num2)):
    print("Los numeros se aman! :loveatfirstsight:")
else:
    print("Los numeros se odian")