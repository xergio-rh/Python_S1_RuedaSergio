##Ejercicio 2: Interest calculator 




def calcular(P, T, Time, F):
   monto_total = (P) * (1 + (T / (100 * F))) ** ( F * Time)
   interes_compuesto = monto_total - P
   return monto_total, interes_compuesto

P= int(input("escribe lo que vas a invertir:"))
Time=  int(input("escribe por cuanto tiempo: "))
T= int(input("ingresa el porcentaje de interes:"))
F=int(input("ingrese la frecuencia:"))

result=calcular(P,T,Time,F)
print (result)



## Desarrollado por: Sergio Rueda / T.I: 1.097.101.293
