# import os, sys

mitexto = open('.\\hola.txt')  # por defecto está en read mode
copia = mitexto.read()
mitexto.close()
print(copia)

mitexto = open('.\\hola.txt')
copia = mitexto.readlines()  # devuelve las lineas como una lista
mitexto.close()
print(copia)

mitexto1 = open('.\\hola2.txt', 'w')  # abre en write mode. Si el archivo existía, lo pisa
mitexto1.write('saraaaasaaaaaaa1\n')
mitexto1.write('saraaaasaaaaaaa2\n')
mitexto1.write('saraaaasaaaaaaa3')
mitexto1.close()

mitexto2 = open('.\\hola2.txt', 'a')  # abre en append mode. Si el archivo existía, agrega contenido
mitexto2.write('\nmas sarasa')
mitexto2.write('\nmas sarasa')
mitexto2.write('\nmas sarasa')
mitexto2.close()

import shelve

shelve1 = shelve.open('diccionario')  # con shelve se crea un archivo de diccionario
shelve1['frutas'] = ['banana', 'manzana', 'ananaá', 'mandarana']
print(shelve1['frutas'])
shelve1.close()
shelve1 = shelve.open('diccionario')
print(shelve1['frutas'])

print(list(shelve1.keys()))
print(list(shelve1.values()))

shelve1.close()
