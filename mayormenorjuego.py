import random

def run ():
    naleatorio=random.randint(0,99)
    numero=int(input("La computadora piensa en un numero aleatorio etre 0 y 99 ¿Puedes adivinar cual es?: "))
    while numero != naleatorio:
        if numero > naleatorio:
            print("El número es más pqueño")
            numero=int(input("Escribe otro numero: "))
        else:
            print("El número es más grande")
            numero=int(input("Escribe otro numero: "))
    
    print("Ganaste")



if __name__=="__main__":
    run()