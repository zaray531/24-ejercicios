sueldo_base=float(input("Ingrese el sueldo base: "))
v1=float(input("venta 1:"))
v2=float(input("venta 2:"))
v3=float(input("venta 3:")) 
comisiones=(v1+v2+v3)*0.10
total=comisiones+sueldo_base
print("Las comisiones son:", comisiones)
print("El sueldo total es:", total)
