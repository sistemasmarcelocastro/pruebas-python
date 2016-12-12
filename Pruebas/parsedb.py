#!/usr/bin/python3

import io, sys, os

######ABRE EL ARCHIVO DE ZONA######
try:
    entrada = str(sys.argv[1])
    archivo = os.path.basename(entrada)
except IndexError:
    print('\nDebe ingresar el nombre de un archivo de zona como argumento\n')
    exit()
try:
    zona = io.open(archivo, encoding='latin-1')
except:
    print('\nEscriba un nombre de archivo de zona correcto\n')
    exit()

######ENCUENTRA LOS REGISTROS "A"######
listaINA = []
for i in zona:
    zonaLinea = i.split()
    zonaLineaJoin = ' '.join(zonaLinea)
    if 'IN A' in zonaLineaJoin and str(zonaLineaJoin[0]) != ';':
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
    # print(listaINA[i][3])
    if int(listaIPrev[i][1]) != int(octeto3):
        originLinea = '$ORIGIN %s.in-addr.arpa.' % ('.'.join(listaIPrev[i][1:]))
        originLineaTupla = (originLinea, listaIPrev[i][1])
        origin.append(originLineaTupla)
        octeto3 = listaIPrev[i][1]

######SALIDA######
# VARIABLES:
quezona = archivo[:-4].strip()
server = 'ns-2.%s' % (quezona)
root = 'admin.dc.uba.ar.'

# ENCABEZADO:
print('''
$TTL    600;
@	IN	SOA		%s	%s(
				2014122200	;serial ->formato yyyymmddxx
				3600
				300
				360000
				600)
	IN	NS		ns-1.dmz.dc.uba.ar.
	IN	NS		ns-2.dmz.dc.uba.ar.
''' % (server, root))

# ORIGIN Y PTR:
for i in range(0, len(origin)):
    print(origin[i][0])
    for j in range(0, len(listaIPrev)):
        if int(listaIPrev[j][1]) == int(origin[i][1]):
            lineaPTR = '%s\tPTR\t%s%s' % (str(listaIPrev[j][0]), str(listaINA[j][0]), quezona)
            print(lineaPTR)