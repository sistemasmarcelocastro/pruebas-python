import re

"""
texto = 'mi numero es 123-456-7890, y también tengo el 444-555-6666'
miregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
enc = miregex.findall(texto)
print(enc)  # objetos regex findall con 0 ó 1 grupo devuelven una lista de las coincidencias

texto2 = 'mi numero es 123-456-7890, y también tengo el 444-555-6666'
miregex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
enc2 = miregex2.findall(texto2)
print(enc2)  # objetos regex findall con más de 1 grupo devuelven una lista de tuplas con las coincidencias
"""
"""
miregex3=re.compile(r'(0|1|2|3|4|5|6|7|8|9)')
miregex4=re.compile(r'\d')#es lo mismo que lo anterior. \d es dígito numérico
miregex5=re.compile(r'\D')#\D es dígito NO numérico
miregex6=re.compile(r'\w')#\w es letras, números y guiones bajos (_)
miregex7=re.compile(r'\W')#\w es NO letras, números y guiones bajos (_)
miregex8=re.compile(r'\s')#\s es espacios, tabs o nuevas lineas
miregex9=re.compile(r'\S')#\s es NO espacios, tabs o nuevas lineas

"""

texto = '10 sarasa sarasa, 11 pepe pepito, 10 recontra sarlanga, 9 super vaca, 8 petetes pututos'
miregex10 = re.compile(r'\d+\s+\w+')
enc10 = miregex10.findall(texto)
print(enc10)

vocales = re.compile(r'[aeiouAEIOU]')  # [] significa "cualquiera de" y acepta enumeraciones y rangos
encvoc = vocales.findall(texto)
print(encvoc)
conso = re.compile(r'[^aeiouAEIOU]')  # el ^ es un NOT
enccon = conso.findall(texto)
print(enccon)
