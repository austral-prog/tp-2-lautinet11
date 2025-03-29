#Variables
Gasto = 23.75
Ingreso = 100
Vueltop = 0
VUeltoc = 0

print("Ingresar gasto:")
print(Gasto) # Deveria ser un input ( Pero sirve para demostrar asi)
print("Dinero recibido")
print(Ingreso) # Deveria ser un input (Sirve para chequear nomas asi)
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
