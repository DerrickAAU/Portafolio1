"""
Nombre: Divisores de un numero
Entrada: numero a buscar divisores
Salida: Los divisores del numero
Resticciones: Que sea un numero entero positivo
              Que sea un numero positivo
              Que sea un numero mayor a cero
"""
def divisores(num):
    if isinstance(num,int):
        if num>0:
            return div_aux(num,num)
        else:
            print("El numero tiene que ser mayor a cero")
    else:
        print("El numero tiene que ser entero")
        

def div_aux(num,i):   
    if i==0:
        return None
    else:
        if(num%i)==0:
            print(i)
        return div_aux(num,i-1)

#-------------------------------------------------------------------
"""
Nombre: Multiplicar sin operador
Entrada: num:numero a multlicar  factor: numero por el que se multiplicará
Salida: Resultado de la multiplicacion
Resticciones: Que sea un numero entero positivo
              Que sea un numero positivo
              Que sea un numero mayor a cero
"""

def multiplicarRecursivo(num,factor):
    if isinstance(num,int) and isinstance(factor,int):
        if num>=0 and factor>=0:
            return multi_aux(num,factor)
        else:
            print("Error: El numero tiene que ser postivo mayor a cero")
    else:
        print("Error: El numero tiene que ser entero positivo")
        

def multi_aux(num,factor):
    if factor==0:
        return 0
    else:
        return num+multi_aux(num,factor-1)

#-----------------------------------------------------------------------

"""
Nombre: DivisionRecursivo
Entrada: divisor y Diviendo, digitos a dividir y el Dividendo
Salida: El resultado de la división
Restricciones: Que sea un numero entero positivo
               Que sea un numero positivo
               Que sea un numero mayor a cero
"""

def divisionRecursivo(divisor,Dividendo):
    if(isinstance(divisor,int) and isinstance(Dividendo,int)):
        return divisionRecursivo_aux(divisor,Dividendo,0)
    else:
        return ("El número debe ser entero positivo")

def divisionRecursivo_aux(divisor,Dividendo,contador):
    if (contador<=divisor):
        return 0
    elif (contador>divisor):
        return -1
    else:
        return(1+divisionRecursivo_aux(divisor,dividendo,contador+dividendo))

#------------------------------------------------------------------------
"""
Nombre: Pasar a entero
Entrada: Numero decimal
Salida: El numero convertido en entero
Restricciones: Que sea un numero decimal positivo
               Que sea un numero positivo
               Que sea un numero mayor a cero
"""

def corrimientoAEntero(n):
    if isinstance(n,float):
        n = n%10**10*10000000
        n = int(n)
        return corrimientoAEntero_aux(n,0)
    else:
        return ("Error: Deben ser numeros con decimal")

def corrimientoAEntero_aux(n,posicion):
    if n%10 == 0 and n!=0:
        return corrimientoAEntero_aux(n//10,posicion)
    if n==0:
        return 0
    else:
        return(n%10*10**posicion + corrimientoAEntero_aux(n//10,posicion+1))



#-----------------------------------------------------------------------
"""
Nombre: Contar digitos decimales
Entrada: El numero a evaluar
Salida: La cantidad de digitos contando los decimales
Restricciones: Que sea un numero decimal positivo
               Que sea un numero positivo
               Que sea un numero mayor a cero
"""

def contarDigitoFlotante(digito):
    if isinstance(digito,float) and (digito>0):
        digito = digito%10**10*10000000
        digito = int(digito)
        return(contarDigitoFlotante(digito))
               
    elif digito==0:
        return 0
    elif digito<0:
        return contarDigitoFlotante(digito*-1)
    elif digito%10==0:
        return contarDigitoFlotante(digito//10)
    elif digito>0:
        return 1+contarDigitoFlotante(digito//10)
    else:
        return "Error: El digito ingresado es erroneo"





#---------------------------------------------------------------------
"""
Nombre: Indice del numero digitado
Entrada: Numero e indice, numero y la posicion que desea extraer
Salida: El numero del indice del numero ingresado
Restricciones: Que sea un numero entero positivo
               Que sea un numero positivo
               Que sea un numero mayor a cero
"""

def iNum(numero,i):
    if (isinstance(numero, int) and numero>0 and isinstance(i, int)):
        
        recorrido = numDigitos(numero)
        fc = numero-1
        
        return iNum_aux(numero,i+1,fc,recorrido)
    
    else:
        return "Error: El numero ingresado debe ser entero"



def numDigitos(numero):
    if (numero==0):
        return 0
    else:
        return(1+numDigitos(numero//10))


def iNum_aux(numero,i,fc,recorrido):
    if numero==0:
        return 0
    else:
        if numero<fc:
            return numero%10+iNum_aux(numero%10//10,i,fc,recorrido)
        elif i==recorrido:
            return (numero%10)+iNum_aux(numero%10//10,i,fc,recorrido)
        else:
            recorrido = recorrido-i
            return(iNum_aux(numero//10**recorrido,i,fc,recorrido))





#-------------------------------------------------------------------
                   
"""
Nombre: Cortar un numero
Entrada: Numero, y los indices, las partes a cortar
Salida: El numero cortado, los numeros segun el indice que desea
Restricciones: Que sea un numero entero positivo
               Que sea un numero positivo
               Que sea un numero mayor a cero
"""

def cortarNumero(numero,i1,i2):
    if(isinstance(numero,int) and (numero>0)):
       if isinstance(i1,int) and isinstance(i2,int):
           if (i1>=0) and (i2>=0):
               num1 = iNum(numero,i1)
               num2 = iNum(numero,i2)
               return cortarNumero_aux(num1,num2)
            
           else:
              return "Los indices deben ser mayores o igual a cero"
       else:
           return "Digite un numero entero"
    else:
        return "Digite un numero entero"

def cortarNumero_aux(num1,num2):
    if num1==0:
        return 0
    else:
        return num1*10+num2+cortarNumero_aux(num1//10,num2)
    



