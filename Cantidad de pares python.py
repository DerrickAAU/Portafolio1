def cantidadDePares(num):
    if(isinstance(num,int) and num >0):
        return cantidadDePares_aux(num,0)
    else:
        return 'dijite un numero entero positivo'

def cantidadDePares_aux(numVerified,result):
    if(numVerified ==0):
        return result
    elif(numVerified % 2 ==0):
        return cantidadDePares_aux(numVerified//10, result=result+1)
    else:
        return cantidadDePares_aux(numVerified//10, result)
