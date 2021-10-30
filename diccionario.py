def run():
    poblacion_pais ={
        'Argentina': 431232332,
        'Brasil': 232323,
        'Colombia': 2323244,
    }

    print (poblacion_pais)

    for pais in poblacion_pais.keys():
        print(pais)

    for pais in poblacion_pais.values():
        print(pais)

    for pais in poblacion_pais.items():
        print(pais)

    for pais, poblacion in poblacion_pais.items():
        print(pais, poblacion)



if __name__=="__main__":
    run()
