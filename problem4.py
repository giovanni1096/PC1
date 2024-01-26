N = int(input("Ingrese un entero positivo: "))
if N<=0:
    print("Ingrese numero entero positivo")
else:
    suma = (N*(N+1)) // 2

print(f"La suma de los primero {N} enteros positivos es : {suma}")