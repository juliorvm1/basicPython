def es_palindromo(palabra):
    # Quitarle los espacios a la palabra
    palabra=palabra.replace(" ","")
    # convertir todos los caracteres a minusculas
    palabra=palabra.lower()
    # recorrer los caracteres de la palabra alreves usando slides y compararlos
    if palabra[::] == palabra[::-1]:
        return True
    else:
        return False
    

def run ():
    palabra=input("Escribe una palabra: ")
    if es_palindromo (palabra):
        print(palabra, " Es palindromo ")
    else:
        print(palabra, " No es palindromo")


if __name__=="__main__":
    run()