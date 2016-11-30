#Encontrar patrones en un texto
#sin RegEx:
""" Sin RegEx
def estel(entrada):
    if len(entrada) != 12:
        return False  # longitud incorrecta
    for i in range(0, 3):
        if not entrada[i].isdecimal():
            return False  # no hay prefijo
    if entrada[3] != '-':
        return False  # no tiene guión
    for i in range(4, 7):
        if not entrada[i].isdecimal():
            return False  # no hay primeros 3 digitos
    if entrada[7] != '-':
        return False  # no hay segundo guion
    for i in range(8, 12):
        if not entrada[i].isdecimal():
            return False  # no hay últimos 4 digitos
    return True


def enctel(entrada):
    seEncontro = False
    for i in range(len(entrada)):
        pedazo = entrada[i:i + 12]
        if estel(pedazo):
            print('se encontró el tel: ' + pedazo)
            seEncontro = True
    if not seEncontro:
        print('No hay teléfonos en el texto')


entrada = 'asdlkasdjf 123-456-7890 skskdowo d wd dw ñ...c 789-456-1235.dwwd wd w wd wd444-555-6666...'

enctel(entrada)


# print(entrada)
# print(estel('123-456-7890'))
"""
# Con RegEx:
import re

entrada = 'asdlkasdjf 123-456-7890 skskdowo d wd dw ñ...c 789-456-1235.dwwd wd w wd wd444-555-6666...'
numtelRe = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # crea un objeto "re" con el patrón
print(numtelRe.findall(entrada))# encuentra todas las coincidencias con el patrón.
