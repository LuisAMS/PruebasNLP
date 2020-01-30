#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 17:02:37 2020

@author: luisams
"""
def generaArchivo(entrada,tunning,dev):
    archivoTunn =  open(tunning, 'w')
    archivoDev  = open(dev, 'w')
    contador = 0
    with open(entrada) as f:
        for linea in f:
            if contador%2 == 0:
                archivoTunn.write(linea)
            else:
                archivoDev.write(linea)
            contador += 1
    archivoTunn.close()
    archivoDev.close()
    
                

archivo1 = 'dev.spa'
archivo2 = 'dev.por'

tunning1 = 'corpusSal/tunning.es'
tunning2 = 'corpusSal/tunning.pt'

dev1 = 'corpusSal/dev.es'
dev2 = 'corpusSal/dev.pt'

generaArchivo(archivo1, tunning1,dev1)
generaArchivo(archivo2, tunning2,dev2)

