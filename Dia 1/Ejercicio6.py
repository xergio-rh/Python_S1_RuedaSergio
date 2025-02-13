##Ejercicio 6: Programa para calcular los sueldos de una empresa

n=int(input("Ingresa la cantidad de empleados"))
totalBruto=int
totalEPS=int
totalPension=int
totalNeto=int
mayorSueldo=0
menorSueldo=0

for i in range (n-1):
    nombre=(input("Ingrese el nombre del empleado",i,":"))
    horas=int(input("Ingrese las horas trabajadas"))
    bruto=horas*20000
    eps=bruto*0.04
    pension=bruto*0.04
    neto=bruto-eps-pension

    totalBruto=totalBruto+bruto
    totalEPS=totalEPS+eps
    totalPension=totalPension+pension
    totalNeto=totalNeto+neto

    if neto>mayorSueldo:
        mayorSueldo=neto
        nombreMayor=nombre
    if neto <mayorSueldo:
        menorSueldo=neto
        nombreMenor=nombre
    
    print("Empleado",nombre)
    print("Sueldo Bruto: $",bruto)
    print("EPS: $",eps)
    print("Pension: $",pension)
    print("Sueldo Neto: $",neto)


promedioBruto=totalBruto/n
promedioNeto=totalNeto/n

print("Totales:")
print("Total salarios brutos: $",totalBruto)
print("Total EPS: $",totalEPS)
print("Total Pension: $",totalPension)
print("Total salarios netos: $",totalNeto)
print("Empleado que mas gana: $",nombreMayor)
print("Empleado que menos gana: $",nombreMenor)
print("Promedio salarios brutos: $",promedioBruto)
print("Promedio salarios netos: $",promedioNeto)

##Desarrollado por: Sergio Rueda / T.I: 1.097.101.293
