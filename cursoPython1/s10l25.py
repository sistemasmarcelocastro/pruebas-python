import re

"""
patron = re.compile(r'Bat(wo)?man')  # el ? significa cero o una vez
patron = re.compile(r'Bat(wo)*man')  # el * significa cero o más veces
patron = re.compile(r'Bat(wo)+man')  # el + significa una o más veces
patron = re.compile(r'Bat(wo){3}man')  # el {n} significa exactamente n veces
patron = re.compile(r'Bat(wo){3,5}man')  # el {n,m} significa un rango de veces entre n y m
# los () se pueden nestear


coincidencias = patron.search('Las aventuras de Batwoman')
print(coincidencias.group())
"""
"""
telRe = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d')  # el ? significa cero o una vez
enctel = telRe.search('mi número es 123-456-7890')
print(enctel.group())
enctel2 = telRe.search('mi número es 456-7890')
print(enctel2.group())
"""

miregex = re.compile(r'(\d){3,5}')
enc = miregex.search(
    '1234567890')  # python, por defecto hace "greedy match", o sea que encuentra el rango más largo posible y lo antes posible
print(enc.group())

miregex2 = re.compile(r'(\d){3,5}?')  # agregando el ? se hace un non-greedy match
enc2 = miregex2.search('1234567890')
print(enc2.group())
