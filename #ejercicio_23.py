#ejercicio_23.py

from ctypes.wintypes import HACCEL
import modulo_arbol

import collections

arbol_de_criaturas = modulo_arbol.nodoArbol()

CRIATURAS = [
    {"nombre": "Ceto","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Tifón","derrotado_por": "Zeus", "descripcion": None, 'capturado_por': None},
    {"nombre": "Equidna","derrotado_por": "Argos Panoptes", "descripcion": None, 'capturado_por': None},
    {"nombre": "Dino","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Pefredo","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Enio","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Escila","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Caribdis","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Euríale","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Esteno","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Medusa","derrotado_por": "Perseo", "descripcion": None, 'capturado_por': None},
    {"nombre": "Ladón","derrotado_por": "Heracles", "descripcion": None, 'capturado_por': None},
    {"nombre": "Aguila del Cáucaso","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Quimera","derrotado_por": "Belerofonte", "descripcion": None, 'capturado_por': None},
    {"nombre": "Hidra de Lerna","derrotado_por": "Heracles", "descripcion": None, 'capturado_por': None},
    {"nombre": "León de Nemea","derrotado_por": "Heracles", "descripcion": None, 'capturado_por': None},
    {"nombre": "Esfinge","derrotado_por": "Edipo", "descripcion": None, 'capturado_por': None},
    {"nombre": "Dragón de Cólquida","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Cerbero","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Cerda de Cromión","derrotado_por": "Teseo", "descripcion": None, 'capturado_por': None},
    {"nombre": "Ortro","derrotado_por": "Heracles", "descripcion": None, 'capturado_por': None},
    {"nombre": "Toro de Creta","derrotado_por": "Teseo", "descripcion": None, 'capturado_por': None},
    {"nombre": "Jabalí de Calidón","derrotado_por": "Atalanta", "descripcion": None, 'capturado_por': None},
    {"nombre": "Garcinos","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Gerión","derrotado_por": "Heracles", "descripcion": None, 'capturado_por': None},
    {"nombre": "Cloto","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Láquesis","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Atropos","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Minotauro de Creta","derrotado_por": "Teseo", "descripcion": None, 'capturado_por': None},
    {"nombre": "Harpías","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Argos Panoptes","derrotado_por": "Hermes", "descripcion": None, 'capturado_por': None},
    {"nombre": "Aves del Estínfalo","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Talos","derrotado_por": "Medea", "descripcion": None, 'capturado_por': None},
    {"nombre": "Sirenas","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Pitón","derrotado_por": "Apolo", "descripcion": None, 'capturado_por': None},
    {"nombre": "Cierva de Cerina","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Basilisco","derrotado_por": None, "descripcion": None, 'capturado_por': None},
    {"nombre": "Jabalí de Erimanto","derrotado_por": None, "descripcion": None, 'capturado_por': None},
]


for c in CRIATURAS:
    modulo_arbol.insertar_nodo(arbol_de_criaturas, c['nombre'], {'derrotado_por': c['derrotado_por'], 'descripcion': c['descripcion'], 'capturado_por': c['capturado_por']})


#A
print("LISTADO DE LAS CRIATURAS Y QUIENES LAS DERROTARON:")
modulo_arbol.inorden_criaturas_derrotadas(arbol_de_criaturas)

#B
print('                                                           ')
modulo_arbol.setDescripcion(arbol_de_criaturas)
#C
print('                                                           ')
nodo_buscado = modulo_arbol.busqueda(arbol_de_criaturas, "Talos")
print("Informacion de Talos: ", nodo_buscado)

#D
print('                                                           ')
vec_heroes = modulo_arbol.obtener_heroes(arbol_de_criaturas)   # Obtengo un vector con todos los heroes y 
                                                            # estarán repetidos si derrotó a más de una criatura

cantidades = collections.Counter(vec_heroes)  # Devuelve un diccionario con el nombre del heroe 
                                              # y la cantidad de recurrencias en el vector
print('                                                           ')
print("HEROES QUE MAS CRIATURAS DERROTARON: ")
for i in range(3): 
    h = (max(cantidades, key=cantidades.get))       # Obtengo del diccionario el heroe que mas criaturas derroto
    cantidad_h = cantidades[h]                      # El numero de criaturas que derrotó
    print(h, "ha derrotado a", cantidad_h, "criaturas")
    cantidades.pop(h)

    continuar = True
    while(continuar == True):   
        if(len(cantidades) > 0):  
            new_h =  max(cantidades, key=cantidades.get)       # Control de si hay más heroes con la misma cantidad de criaturas derrotadas
            if (cantidades[new_h] == cantidad_h):
                print(new_h, "tambien derrotó a", cantidades[new_h], "criaturas.")
                cantidades.pop(new_h)
            else:
                continuar = False
        else: continuar = False

#E
print('                                                           ')
print('criaturas derrotadas por Heracles son:')
modulo_arbol.derrotados_por_Heracles(arbol_de_criaturas)
#F
print('                                                           ')
print('las criaturas no derrotadas son:')
modulo_arbol.criaturas_que_aun_no_derrotaron (arbol_de_criaturas)
#G
print('                                                           ')

#H
print('                                                           ')
buscado = modulo_arbol.busqueda(arbol_de_criaturas, 'Cerbero')
buscado['datos']['capturado_por'] = 'Heracles'
buscado = modulo_arbol.busqueda(arbol_de_criaturas, 'Toro de Creta')
buscado['datos']['capturado_por'] = 'Heracles'
buscado = modulo_arbol.busqueda(arbol_de_criaturas, 'Cierva de Cerina')
buscado['datos']['capturado_por'] = 'Heracles'
buscado = modulo_arbol.busqueda(arbol_de_criaturas, 'Jabalí de Erimanto')
buscado['datos']['capturado_por'] = 'Heracles'
#I
print('                                                           ')
while(opcion == 'n'):
    clave = input("Ingrese parte de lo que desea buscar: (Mayúscula al inicio): ")
    buscado = modulo_arbol.busqueda_por_proximidad(arbol_de_criaturas, clave)
    print(buscado['info'])
    opcion = input("Es esta la criatura buscada? s/n: ")
#J
modulo_arbol.eliminar_nodo(arbol_de_criaturas, 'Basilisco')
modulo_arbol.eliminar_nodo(arbol_de_criaturas, 'Sirenas')
#k
print('                                                           ')
nodo_aves = modulo_arbol.busqueda(arbol_de_criaturas, 'Aves del Estínfalo')
nodo_aves['datos']['derrotado_por'] = 'Heracles ha derroatado a varias'
#L
print('                                                           ')
nodo_ladon = modulo_arbol.busqueda(arbol_de_criaturas, 'Ladón')
modulo_arbol.insertar_nodo(arbol_de_criaturas, 'Dragón de Ladón', {'derrotado_por': nodo_ladon['datos']['derrotado_por'], 'descripcion': nodo_ladon['datos']['descripcion'], 'capturado_por': nodo_ladon['datos']['capturado_por']})
modulo_arbol.eliminar_nodo(arbol_de_criaturas, 'Ladón')
#M
print('                                                           ')

#N
print('                                                           ')
print('criaturas derrotadas por Heracles son:')
modulo_arbol.derrotados_por_Heracles(arbol_de_criaturas)
