# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import codecs
import re
from re import UNICODE
import operator
    
def preprocesaTexto (texto):
    texto2 = texto.lower ()
    patron = re.compile ('[^\w ]+', UNICODE)
    texto2 = re.sub (patron, '', texto2)
    return texto2
        
def separaEnPalabras (c):
    controlPrevio = 0
    lista = []
    for x in range (0, len(c) ):
        if c[x] == " ":
            palabra = c [controlPrevio : x]
            lista.append (palabra)
            controlPrevio = x + 1
    return lista
    
def creaDiccionario (lista):
    listaPalabras = sorted (set (lista))
    diccionario = {}
    for x in range (0, len(listaPalabras)):
        diccionario [listaPalabras[x]] = 0
    for palabra in diccionario:
        for y in range (0, len(lista)):
            if palabra == lista [y]:
                diccionario [palabra] += 1      
    return diccionario
    
    
archivo = codecs.open("/Users/luisams/Documents/hello.txt","r","utf-8") 
a = archivo.read ()
c = preprocesaTexto (a)
lista = separaEnPalabras (c)
diccionario = creaDiccionario (lista)
resultado = sorted (diccionario.items() , key=operator.itemgetter(1))

for x in range(0, len(resultado)):
    indice = len(resultado) - x - 1
    print (resultado[indice][0] + " " + str(resultado[indice][1])) 


