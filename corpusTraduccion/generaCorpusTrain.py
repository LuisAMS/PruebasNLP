#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:15:08 2020

@author: luisams
"""

def generaArchivo(entradas, salida):
    archivoSalida = open(salida,'w')
    for nombre in archivoInN:
        archivo =  open(nombre,'r')
        texto = archivo.read()
        archivoSalida.write(texto)
        archivoSalida.flush()
        archivo.close()
    archivoSalida.close()
        
        
        
    

archivoInN = ['europarl.es','JRC-Acquis.es-pt.es', 'wikititles.es','news.es']

archivoOutN =[ 'europarl.pt','JRC-Acquis.es-pt.pt','wikititles.pt','news.pt']

salida1 = 'corpusSal/train.es'
salida2 = 'corpusSal/train.pt'

generaArchivo(archivoInN, salida1)
generaArchivo(archivoOutN, salida2)

    
    

