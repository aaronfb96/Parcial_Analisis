from ast import operator
from re import X

# Lista con Diccionarios
dir = [{'numero1':6,'numero2':3,'Op':"Multiplicacion"},{'numero1':4,'numero2':5,'Op':"Resta"}]

# Impresión Diccionarios
print(dir)

#Operacion Multiplicación
def Operaciones(x): 
    x=(dir[0])
    x=list(x.values())
    x=(x[0]*x[1])
    print("El resultado de la multiplicación es: ",x)
    
#Impresión Multiplicación
Operaciones(X) 

#Operacion Resta
def Operaciones(x):
    x=(dir[1])
    x=list(x.values())
    x=(x[0]-x[1])
    print("El resultado de la resta es: ",x)

#Impresión resta
Operaciones(X)


   


    

