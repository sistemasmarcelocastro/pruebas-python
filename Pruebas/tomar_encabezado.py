#!/usr/bin/python3

import io, sys, os

# reverso_original = io.open('inv.dc.uba.ar.zone.rev', encoding='latin-1')


# with io.open('zonas/inv.dc.uba.ar.zone.rev', encoding='latin-1') as origen:
# with open('zonas/inv.dc.uba.ar.zone.rev', 'r') as origen:
buscar = 'NS'
lineaFinalEnc = 0
origen = io.open('zonas/inv.dc.uba.ar.zone.rev', encoding='latin-1')
enum = enumerate(origen, 1)
for num, linea in enum:
    if buscar in linea:
        lineaFinalEnc = num
origen.close()
origen = io.open('zonas/inv.dc.uba.ar.zone.rev', encoding='latin-1')
listaOrigen = origen.read().split(sep='\n')
for i in range(0, lineaFinalEnc):
    print(listaOrigen[i])
origen.close()

'''
    for i in range(1,int(lineaFinalEnc)+1);
        bbb=origen.next().strip()
        #print(i)

'''
