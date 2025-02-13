##Ejercicio 3: Number Classification

import math

def clasificar(n):
    if n < 0:
        return "El número no puede ser negativo"
    


    par_impar = "par" if n % 2 == 0 else "impar"



    if n < 2:
        print("no es primo ni compuesto") 
    else:
        for i in range (2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                tipo = "compuesto"
        else:
            tipo = "primo"
    
    

    raiz = int(math.sqrt(n))
    cuadrado_perfecto = "es un cuadrado perfecto" if raiz * raiz == n else "no es un cuadrado perfecto"
    
    return f"El número {n} es {par_impar}, {tipo}, y {cuadrado_perfecto}."



numero =int(input("Escribe un numero:"))
resultado = clasificar(numero)
print(resultado)


## Desarrollado por: Sergio Rueda / T.I: 1.097.101.293
