salario_base=float(input("Ingrese su salario base: "))
comision = salario_base * 0.10
comision_final = comision * 3
print("La comisión que obtendrá por las tres ventas del mes será de:",comision_final)
print("El total del salario incluyendo las comisiones es de:", salario_base + comision_final)