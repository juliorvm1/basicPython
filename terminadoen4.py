def run ():
    dato=int(input("Escribe un numero entero y te dire si termina en 4: "))
    cadena=str(dato)
    print(cadena[len(cadena)-1])
    if cadena[len(cadena)-1]=='4':
        print("el numeor entero termina en 4")
    else:
        print("el numeor entero no termina en 4")


if __name__=="__main__":
    run()
