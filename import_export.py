#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
# exportar archivo
def write_csv(nombre_archivo, lista_data, inicio=False):
    if inicio:
        tipo = 'w'
    else:
        tipo = 'a'
    with open(nombre_archivo, tipo) as output:
        writer = csv.writer(output, delimiter=";", quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        for i in lista_data:
            writer.writerow([i])