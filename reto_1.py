

consecionario = []

def RegistrarAuto ():
    marca = input("ingrese la marca del carro: ")
    modelo = input("ingrese el modelo del carro registrado: ")
    valor  = float(input("ingrese el valor del carro: "))

    carro = { "Marca": marca, "Modelo": modelo, "Precio": valor}
    consecionario.append(carro)

    print("el carro ha sido registrado correctamente")

def Verautos():
    if not consecionario:
        print("en el consencionario no hay carros o no hay ninguno regustrado")
    else:
        print("--------- los carros registrados son los siguientes:--------------- ")
        for i, j in enumerate(consecionario,1 ):
            print(f"{i}. Marca: {j['Marca']} -  Modelo: {j['Modelo']} -  Valor: {j['Precio']}")


def Buscarautos():
    carro  = input("ingrese la marca del carro que desea bsucar: ")
    buscar = [i for i in consecionario if carro == i['Marca'].lower()]

    if buscar:
        for i in buscar:
            print(f"Marca: {i['Marca']} - Modelo: {i['Modelo']} - Valor: {i['Precio']}")

    else:
        print("no se encontro un carro con la marca: {carro} registrado ")

def Valorinventario():
    Calculo = [i['Precio'] for i in consecionario]
    valor_total = sum(Calculo)

    print(f" Hay un total de: {valor_total} COP invertidos en el conce ")

def Eliminarauto():

    carro = input("ingrese la marca del carro que desea eliminar: ").lower()

    for i, j in enumerate(consecionario):
        if carro == j['Marca'].lower():
            consecionario.pop(i)
            print("el carro {carro} ha sido eleminado con exito ")

        else:
            print("no se encontre un carro con esa marca dentro del conseccionario")


def Menu():
    while True:
        print("\n----------- ingresa la operacion que deseas realizar ----------- ")
       
        print("ingrese 1 si desea registrar carros. ")
        print("ingrese 2 si desea ver todos los carros que posee el inventario. ")
        print("ingrese 3 si desea buscar un carro. ")
        print("ingrese 4 si desea ver el valor total del inventario ")
        print("ingrese 5 si desea eliminar un auto del inventario ")
        print("ingrese 6 si desea salir ")

        opcion = input("ingrese la operacion que desea realizar (1-5):  ")

        if opcion == "1":
            RegistrarAuto()
        elif opcion == "2":
            Verautos()
        elif opcion == "3":
            Buscarautos()
        elif opcion == "4":
            Valorinventario()
        elif opcion == "5":
            Eliminarauto()
        elif opcion == "6":
            print("saliste del programa ")
            break

        else: 
            print("primo, son numeros del (1-5)")


Menu()


