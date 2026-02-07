num1= int(input("Escribe un número:"))
num2= int(input("Escribe otro número:"))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2

print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multi)

if num2 != 0 :
    div = num1/num2
    print("La división es:",div)
else:
    print("No se puede dividir entre cero")