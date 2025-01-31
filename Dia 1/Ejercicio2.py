##Ejercicio 2: Programa que resuelva la siguiente serie hasta N 
##    1-(1/2)+(1/3)-(1/4)...+-(1/N)


cantidad_terminos = int(input("Ingrese la cantidad de terminos: "))
print(f"La cantidad de terminos son: {cantidad_terminos}")

if cantidad_terminos <= 0:
    print(0)
else:
    sumatoria = 0.0
    
for i in range(1, cantidad_terminos + 1):
    if i % 2 == 0:
        sumatoria = sumatoria - (1 / i)  
    else:
        sumatoria = sumatoria + (1 / i)  

print("La sumatoria dio:", sumatoria)

## Desarrollado por: Sergio Rueda / T.I: 1.097.101.293