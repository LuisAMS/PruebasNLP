#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:14:26 2020

@author: luisams
"""
import sys


argumentos = sys.argv
archivoOrigen = str(argumentos[1])
archivoSalida1 = str(argumentos[2])
archivoSalida2 = str(argumentos[3])

salida1 = open(archivoSalida1, 'w')
salida2 = open(archivoSalida2, 'w')
print(archivoOrigen)
with open(archivoOrigen) as f:
    for linea in f:
        texto = linea.split('\t')
        salida1.write(texto[0]+'\n')
        salida2.write(texto[1])
        salida1.flush()
        salida2.flush()
        
salida1.close()
salida2.close()
#archivoOrigen.close()


