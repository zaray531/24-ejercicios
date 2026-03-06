compra=float(input("valor de la compra: "))
descuento=compra*0.10
subtotal=compra-descuento
iva=subtotal*0.19
total=subtotal+iva
print("iva:", iva)
print("total:", total)
