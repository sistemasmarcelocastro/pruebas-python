#!/usr/bin/python3

import sys

argumentos = sys.argv

# Capturar error en el argumento:
try:
    labo = int(argumentos[1])
except:
    print('\n\n\nEl único argumento válido es el número del laboratorio (1-7)\n\n\n')
    exit()
if not 1 <= labo <= 7:
    print('\n\n\nNúmero de laboratorio incorrecto (1-7)\n\n\n')
    exit()

# Componer el nombre del laboratorio:
laboNombre = 'labo' + str(labo) + '.txt'

# Abrir archivos:
laboNtxt = open(laboNombre, 'w')  # archivo que se va a escribir
# origen = open('/var/log/maquinas.log')  # el log de checkLabos
origen = open('maquinas.log')  # Log de prueba

# Extraer la última linea del log y remover la fecha:
lineas = origen.readlines()
ultimaLinea = lineas[-1]
soloMaquinas = str(ultimaLinea.split()[2])

# Imprimir la fecha de verificación
soloFecha = str.join(' - ', ultimaLinea.split()[:2])
print('''
Última verificación: %s
\nMáquinas corriendo Linux:
''' % (soloFecha))

# Seleccionar porción del string según el labo:
inicio = (labo - 1) * 25
final = inicio + 25
todas = str(soloMaquinas[inicio:final])

# Encontrar máquinas prendidas y escribir las IP's en el archivo labo[n].txt:
num = 1  # último octeto de la IP
for i in todas:
    if i == 'L':
        print('ws%slab%s' % (num, labo))
        laboNtxt.write('10.2.%s.%s\n' % (labo, num))
    num += 1
print()
# Cerrar archivos:
laboNtxt.close()
origen.close()
