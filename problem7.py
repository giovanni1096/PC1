def mostrar_menu():
    print("Menu:")
    print("1. Mostrar la suma de los dos números")
    print("2. Mostrar la resta número)")
    print("3. Mostrar la multiplicación de los dos números")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

mostrar_menu()

opcion = input("Seleccione una opción (1, 2 o 3): ")

if opcion == "1":
    resultado = num1 + num2
    print(f"La suma de los dos números es: {resultado}")
elif opcion == "2":
    resultado = num1 - num2
    print(f"La resta (primer número menos segundo número) es: {resultado}")
elif opcion == "3":
    resultado = num1 * num2
    print(f"La multiplicación de los dos números es: {resultado}")
else:
    print("Opción inválida. Por favor, seleccione 1, 2 o 3.")