# diccionarios
"""
gato = {'tamaño': 'gordo', 'color': 'blanco', 'animo': 'apapachero'}
print(gato['tamaño'])

for k, v in gato.items():
    print(k + ' contiene ' + v)
"""
import pprint

mensaje = 'Qué lehabrán hacho mis manos, qué le habrán hecho...'
cuenta = {}
for letra in mensaje.upper():
    cuenta.setdefault(letra, 0)
    cuenta[letra] = cuenta[letra] + 1
pprint.pprint(cuenta)
