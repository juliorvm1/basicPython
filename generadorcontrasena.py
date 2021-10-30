
import string
import random



def generar_contrasena():
    minusculas=list(string.ascii_lowercase)
    mayusculas=list(string.ascii_uppercase)
    numeros=[]
    caracteres= ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    for i in range(11):
        numeros.append(str(i))
    
    caracteres=minusculas+mayusculas+numeros+caracteres
    contrasena=[]

    for i in range(15):
        caracter_random=random.choice(caracteres)
        contrasena.append(caracter_random)
    
    contrasena="".join(contrasena)
    return contrasena

    


def run():   

    contrasena=generar_contrasena()
    print(contrasena)
 


if __name__=="__main__":
    run()