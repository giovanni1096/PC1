lista_original = [1, 1, 2, 3, 4, 4, 5, 1]

lista_sin_duplicados = []
for elemento in lista_original:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)

print("Lista Original:", lista_original)
print("Lista Sin Duplicados:", lista_sin_duplicados)