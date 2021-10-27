menu="""
💰 Binvenido al conversor de monedas a dolares 💰
1.- Pesos colombianos
2.- Pesos argentinos
3.- Pesos mexicanos """

def convertir_pesos_a_dolares(pesos,moneda):
    if moneda=="colombia":
        return pesos*0.00027
    elif moneda== "argentina":
        return pesos*0.010
    elif moneda== "mexico":
        return pesos*0.050

opcion=input(menu)

if opcion == '1':
    print("Elegiste convertir pesos colombianos a dolares")
    pesos=float(input("¿Cuantos pesos colombianos tienes?: "))
    print (pesos, " Pesos colombianos equivalen a ", convertir_pesos_a_dolares(pesos,"colombia"), " dolares")
elif opcion == '2':
    print("Elegiste convertir pesos argentinos a dolares")
    pesos=float(input("¿Cuantos pesos argentinos tienes?: "))
    print (pesos, " Pesos argentinos equivalen a ", convertir_pesos_a_dolares(pesos,"argentina"), " dolares")
elif opcion =='3':
    print("Elegiste convertir pesos mexicanos a dolares")
    pesos=float(input("¿Cuantos pesos mexicanos tienes?: "))
    print (pesos, " Pesos mexicanos equivalen a ", convertir_pesos_a_dolares(pesos,"mexico"), " dolares")
else:
    print("Elije una opción correcta")
