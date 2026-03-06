venta=float(input("valor de la venta: "))
iva=venta*0.19
total=venta+iva
pago=float(input("pago: "))
cambio=pago-total
print("El IVA es:", iva)
print("El total a pagar es:", total)
print("El cambio es:", cambio)
