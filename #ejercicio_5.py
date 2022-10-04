#ejercicio_5.py

#import modulo_arbol

from modulo_arbol import (
    nodoArbol,
    insertar_nodo,
    inorden_villano,
    inorden_empieza_con,
    eliminar_nodo,
    inorden,
    postorden_heroes,
    crear_bosque,
    arbol_vacio,
    contar_heroes,
    contar_nodos,
)

arbol = nodoArbol()


heroes = nodoArbol()
villanos = nodoArbol()
contador = 0

lista = [
    ['iron man', False, 1960],
    ['capitana marvel', False, 1890],
    ['thor', False, 1962],
    ['dotor strange', False, 1961],
    ['thanos', True, 1962],
    ['red skull', True, 1963],
    ['capitan america', False, 2000],
    ['loki', True, 1962],
]

for nombre, villano, anio in lista:
    datos = {'villano': villano,
             'anio_aparicion': anio}
    insertar_nodo(arbol, nombre, datos)


# inorden_villano(arbol)
# print()
# inorden_empieza_con(arbol, 'c')
# print()
# print(contar_heroes(arbol))

# crear_bosque(arbol, heroes, villanos)
while not arbol_vacio(arbol):
    info, datos = eliminar_nodo(arbol, arbol['info'])
    print(info, datos)
    if datos['villano'] == True:
        insertar_nodo(villanos, info)
    else:
        insertar_nodo(heroes, info)


print('heroes')
inorden(heroes)
print()
print('villanos')
inorden(villanos)
print()
print('arbol compleo')
inorden(arbol)
print()

#C
print('                                                           ')

print ('los heroes que empiezan con C son:', inorden_empieza_con (heroes, 'c'))

#D
print('                                                           ')

print ('la cantidad de heroes que hay en el arbol son:', contar_nodos(heroes))

#E
print('                                                           ')


#F
print('                                                           ')

print("Superheroes ordenados de manera descendente:")

arbol.postorden_heroes(heroes)
#G
print('                                                           ')





# clave = input('ingrese parte de lo que desea buscar ')
# inorden_empieza_con(arbol, clave)
# print()
# clave = input('ingrese nombre que desea modificar ')
# pos = eliminar_nodo(arbol, clave)
# if pos:
#     name = input('ingrese nuevo nombre ')
#     insertar_nodo(arbol, name, False)
# else:
#     print('valor no encontrado en el arbol')

# inorden(arbol)
# print()

# postorden_heroes(arbol)