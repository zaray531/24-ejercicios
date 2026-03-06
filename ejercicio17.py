salario=float(input("salario: "))
ahorro=float(input("ahorro mensual: "))
eps=salario*0.125
pension=salario*0.16
total_recibir=salario-ahorro-eps-pension
print("EPS:", eps)
print("Pensión:", pension)
print("Total a recibir:", total_recibir)
