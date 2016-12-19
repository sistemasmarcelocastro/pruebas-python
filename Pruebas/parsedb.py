#!/usr/bin/python3

import io, sys, os, time

######ABRE EL ARCHIVO DE ZONA######
try:
    entrada = str(sys.argv[1])
    archivo = os.path.basename(entrada)
except IndexError:
    print('\nDebe ingresar el nombre de un archivo de zona como parámetro\n')
    exit()
if not str(archivo).endswith('.zone'):
    print('\nDebe ingresar un archivo de zona válido\n')
    exit()

try:
    zona = io.open(entrada, encoding='latin-1')
except:
    print('\nDebe ingresar un nombre de archivo de zona existente\n')
    exit()

######ENCUENTRA LOS REGISTROS "A"######
listaINA = []

for i in zona:
    zonaLinea = i.split()
    zonaLineaJoin = ' '.join(zonaLinea)
    if 'IN A' in zonaLineaJoin and not str(zonaLineaJoin).startswith(';') and not str(zonaLineaJoin).startswith('IN'):
        listaINA.append(zonaLinea)

######CIERRA EL ARCHIVO DE ZONA######
zona.close()

######INVIERTE LAS IP######
listaIPrev = []
for i in range(0, len(listaINA)):
    listaIPlinea = str(listaINA[i][3]).split('.')
    listaIPrevParte = []
    for j in reversed(listaIPlinea):
        listaIPrevParte.append(j)
    listaIPrev.append(listaIPrevParte)

######ARMA LOS ORIGIN######

origin = []
octeto3 = 256
for i in range(0, len(listaIPrev)):
    if int(listaIPrev[i][1]) != int(octeto3):
        originLinea = '$ORIGIN %s.in-addr.arpa.' % ('.'.join(listaIPrev[i][1:]))
        originLineaTupla = (originLinea, listaIPrev[i][1])
        origin.append(originLineaTupla)
        octeto3 = listaIPrev[i][1]

######EXTRAE EL ENCABEZADO DEL REVERSO ACTUAL######
buscar = 'NS'
lineaFinalEnc = 0

if len(sys.argv) < 3:
    zonaReversa = entrada + '.rev'
else:
    zonaReversa = str(sys.argv[2])
try:
    reversaOriginal = io.open(zonaReversa, encoding='latin-1')
except:
    print('\nDebe ingresar un nombre de archivo reverso existente\n')
    exit()
enum = enumerate(reversaOriginal, 1)
for num, linea in enum:
    if buscar in linea:
        lineaFinalEnc = num
reversaOriginal.close()
reversaOriginal = io.open(zonaReversa, encoding='latin-1')
listaOrigen = reversaOriginal.read().split(sep='\n')
reversaOriginal.close()

######SALIDA######
# VARIABLES:
queZona = archivo[:-4].strip(' ')

# ENCABEZADO:
indice = 0
serialViejo = 0
serialNuevo = 0
acumulativo = 0
fechaActual = time.strftime('%y%m%d')
for i in range(0, lineaFinalEnc):
    if 'serial' in listaOrigen[i]:  ### Reemplaza el serial.
        for j in range(0, len(str(listaOrigen[i]))):
            if str(listaOrigen[i])[j].isdigit():
                indice = j
                break
        indiceFinal = indice + 9
        serialViejo = str(listaOrigen[i])[indice:indiceFinal]
        if serialViejo[:-2] == fechaActual:
            serialNuevo = int(serialViejo) + 1
        else:
            serialNuevo = str(fechaActual) + '00'
        print(str(listaOrigen[i]).replace(serialViejo, serialNuevo))
    else:
        print(listaOrigen[i])
print('\n\n\n')

# ORIGIN Y PTR:
for i in range(0, len(origin)):
    print(origin[i][0])
    for j in range(0, len(listaIPrev)):
        if int(listaIPrev[j][1]) == int(origin[i][1]):
            lineaPTR = '%s\tPTR\t%s%s' % (str(listaIPrev[j][0]), str(listaINA[j][0]), queZona)
            print(lineaPTR)
    print(';\n;\n;')
