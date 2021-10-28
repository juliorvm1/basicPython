def buclewhile(limite):
    print("*********** Ejemplo de bucles utilizando la estructura de control while   *******")
    contador=0
    resultado=2**contador
    while resultado<=limite:
        print("2 elevado a la ", contador, " es igual a: ", resultado)        
        contador+=1
        resultado=2**contador

    
def buclefor(limite):
    print("*********** Ejemplo de bucles utilizando la estructura de control for   *******")
    for contador in range(limite):
        resultado=2**contador
        if resultado > limite:
            break    
        print("2 elevado a la ", contador, " es igual a: ", resultado)
        




def run():
    buclewhile(1000)
    buclefor(1000)
    

if __name__=="__main__":
    run()