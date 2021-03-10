
"""
Nombre: Reversa de un  numero 
Entrada: Numeros a digitar para su orden invertido
Salida: El resultado de la inversion de los numeros digitados
Restricciones: Ser positivo, entero, mayor a 0.

"""
def CDN(n):
    if (isinstance(n,int)):
        if(n<0):
            return ("Error: el numero debe ser un entero mayor a 0")
        if(n<10):
            return 1
        else:
            return 1 + CDN(n //10)
    else:
        return ("Error el numero no es entero positivo")


def reversaNum(N):
    if isinstance(N, int):
        if(N >= 0):
            if(N <- 10):
                return N
            else:
                return reversaNum_aux(N, CDN(N))
        else:
            print("Error el numero debe ser positivo")
    else:
        print("El numero debe ser entero")

def reversaNum_aux(N, largo):
    if largo == 0:
        return 0
    else:
        return (N % 10) * (10 ** (largo-1))+ reversaNum_aux(N//10,largo-1)
