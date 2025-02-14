## Ejercicio definir si un año es bisiesto o no

def definirAno (año):
    if año % 4 == 0 or año % 400 == 0:
        return f"año es bisiesto"
    else:
        return "año no bisiesto"
    
año = int(input("Que año deseas saber si es bisiesto o no?: "))
print (definirAno(año))

## Desarrollado por: Sergio Rueda / T.I: 1.097.101.293