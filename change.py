def change():
    # Variables
    Gasto = 23.75
    Ingreso = 100

    print("Ingresar gasto:")
    print(Gasto)  # Debería ser un input (pero sirve para demostrar así)
    print("Dinero recibido")
    print(Ingreso)  # Debería ser un input (sirve para chequear nomás así)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")

    Ingreso = float(Ingreso)
    Gasto = float(Gasto)
    a = Ingreso - Gasto
    a = int(a)
    b = (Ingreso - Gasto)

    print(a)
    print("Centavos:")
    
    c = (b - a) * 100
    c = int(c)
    print(c)
change()
