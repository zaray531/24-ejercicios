precio=float(input("Ingrese el precio del producto: "))
cantidad=int(input("Ingrese la cantidad del producto: "))
descuento=float(input("Ingrese el descuento en porcentaje: "))
subtotal=precio*cantidad
descuento_total=subtotal*(descuento/100)
subtotal_con_descuento=subtotal-descuento_total
iva=subtotal_con_descuento*0.19
total=subtotal_con_descuento+iva
print("Subtotal:", subtotal_con_descuento)
print("IVA:", iva)
print("Total:", total)
