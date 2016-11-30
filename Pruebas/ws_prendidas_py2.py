#!/usr/bin/python2.7

import sys

argumentos = sys.argv

try:
    labo = int(argumentos[1])
except:
    print('\n\n\nEl unico argumento valido es el numero del laboratorio (1-7)\n\n\n')
    exit()
if not 1 <= labo <= 7:
    print('\n\n\nNumero de laboratorio incorrecto (1-7)\n\n\n')
    exit()

laboNombre = 'labo' + str(labo) + '.txt'

laboNtxt = open(laboNombre, 'w')

origen = open('maquinas.log')

lineas = origen.readlines()
ultimaLinea = lineas[-1]
soloMaquinas = str(ultimaLinea.split()[2])

soloFecha = str.join(' - ', ultimaLinea.split()[:2])
print('''
Ultima verificacion: %s
\nMaquinas corriendo Linux:
''' % (soloFecha))

inicio = (labo - 1) * 25
final = inicio + 25
todas = str(soloMaquinas[inicio:final])

num = 1
for i in todas:
    if i == 'L':
        print('ws%slab%s' % (num, labo))
        laboNtxt.write('10.2.%s.%s\n' % (labo, num))
    num += 1
print ''

laboNtxt.close()
origen.close()
