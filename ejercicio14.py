total=0
for i in range(1, 5):
    precio=float(input("Ingrese el precio del producto: "))
    cantidad=int(input("Ingrese la cantidad del producto: "))
    total+=precio*cantidad
iva=total*0.19
total_con_iva=total+iva
print("subtotal:", total)
print("IVA:", iva)
print("Total con IVA:", total_con_iva)
