lista_colores = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']


indices_eliminar = [0, 4, 5]

for indice in sorted(indices_eliminar, reverse=True):
    if 0 <= indice < len(lista_colores):
        lista_colores.pop(indice)

print("Lista Resultante:", lista_colores)