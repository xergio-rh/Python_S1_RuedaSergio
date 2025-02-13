##Ejercicio 1: Conversion de temperatura
## Celsius a Fahrenheit



def conversion(grados):
    faahrenheit= (grados)*(9/5)+(32)
    return faahrenheit


def conver(gradosC):
    celsius= (gradosC - 32)*(5/9)
    return celsius




elegir=int(input("¿Deseas convertir de C a F o de F a C?"))


if elegir==1:
    grados=int(input("Ingrese los grados celsius:"))
    print("Los grados celsius son:",conversion(grados))

if elegir==2:
    gradosC=int(input("Ingrese los grados Fahrenheit:"))
    print("Los grados fahrenheit son:",conver(gradosC))


## Desarrollado por: Sergio Rueda / T.I: 1.097.101.293






    
    