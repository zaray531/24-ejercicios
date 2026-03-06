prestamo=float(input("monto del prestamo: "))
interes_anual=prestamo*0.05
interes_trimestre=interes_anual/4
interes_mes=interes_anual/12
total=prestamo+(interes_anual*5)
print("El interés anual es:", interes_anual)
print("El interés trimestral es:", interes_trimestre)
print("El interés mensual es:", interes_mes)
print("El total a pagar después de 5 años es:", total)
