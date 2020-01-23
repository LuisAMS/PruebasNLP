
import codecs
import re
from re import UNICODE
import operator
    
def preprocesaTexto (texto):
    texto2 = texto.lower ()
    patron = re.compile ('[^\w ]+', UNICODE)
    texto2 = texto2.replace("\n", " ")
    texto2 = re.sub (patron, '', texto2)
    return texto2
        
def separaEnPalabras (c):
    lista = []
    lista = c.split()
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
    
def separaBigramas (lista):
    bigramas = []
    for a in range (0, len(lista) - 1):
        bigrama = lista [a] + " " + lista [a + 1]
        bigramas.append(bigrama)
    return bigramas
    
archivo = codecs.open("/Users/luisams/Documents/hello.txt","r","utf-8") 
salida  = codecs.open("/Users/luisams/Documents/bigramas.txt","w","utf-8")

a = archivo.read ()
c = preprocesaTexto (a)
lista = separaEnPalabras (c)
listaBigramas = separaBigramas (lista)
diccionario = creaDiccionario (listaBigramas)
resultado = sorted (diccionario.items() , key=operator.itemgetter(1))

for x in range(0, len(resultado)):
    indice = len(resultado) - x - 1 
    salida.write (resultado[indice][0] + "   " + str(resultado[indice][1])+ "\n")
salida.flush()
salida.close()
archivo.close()
    
