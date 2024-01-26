precio = float(input("Introduzca costo de la cena: "))
porcentaje_propina = float(input(" Ingrese el porcentaje que desea dejar (%): "))
propina = (porcentaje_propina/100)*precio
print(f"Debe dejar una propina de : ${propina:50}")