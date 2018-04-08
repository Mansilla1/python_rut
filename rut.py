#!/usr/bin/env python
# -*- coding: utf-8 -*-
import import_export

# obtener el dígito verificador de un rut
def digito_verificador(rut):
    producto = [2,3,4,5,6,7] # producto de con el cual se debe multiplicar
    list_rut = list(map(int, str(rut))) # convertir en lista el rut
    list_rut.reverse() # revertir los valores
    contador = 0
    pivote = 0
    for i in list_rut:
        if pivote >= len(producto): # si el pivote pasa la cantidad del largo de producto, se debe reiniciar
            pivote = 0
        contador = contador+(i*producto[pivote])
        pivote += 1
    suma_dig = 11-(contador%11) # obtener el resto menos 11 de la suma
    # definir digito verificador
    if suma_dig == 11:
        verificador = 0
    elif suma_dig == 10:
        verificador = 'K'
    else:
        verificador = suma_dig

    return verificador

# método para generar ruts y exportar en archivo csv (opcional)
def genera_rut(**kwargs):
    # rut autoincremental a partir del numero indicado
    keys = []
    for key in kwargs.keys():
        keys.append(key)
    # cantidad de rut a generar
    if not 'cantidad' in keys: # si no se especifica la cantidad, se generarán 10
        cant_rut = 10
    else:
        cant_rut = int(kwargs['cantidad'])
    # inicio del rut (es autoincremental)
    if not 'inicio' in keys:
        inicio = 1
    else:
        inicio = int(kwargs['inicio'])
    # si se exporta o no
    if not 'csv' in keys:
        exportar = False
    else:
        exportar = kwargs['csv'] # true or false
    
    pivot = 0
    lista_rut = []
    while pivot < cant_rut:
        rut = str(inicio) + '-' + str(digito_verificador(inicio))
        lista_rut.append(rut)
        # autoincrementales
        inicio += 1
        pivot += 1

    if exportar:
        import_export.write_csv('output.csv', lista_rut, True)
    else:
        return lista_rut