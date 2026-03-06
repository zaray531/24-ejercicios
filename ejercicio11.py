parcial_1=float(input("parcial 1:"))
parcial_2=float(input("parcial 2:"))
parcial_3=float(input("parcial 3:"))
examen=float(input("examen final:"))
trabajo=float(input("trabajo final:"))
promedio_parciales=(parcial_1+parcial_2+parcial_3)/3
nota_definitiva=promedio_parciales*0.55+examen*0.30+trabajo*0.15
print("La nota definitiva es:", nota_definitiva)
