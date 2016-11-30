import re

texto = 'este es el auto de Al Pacino, pero a hora lo usan Alicia y Alejandro'
patron = re.compile(r'Al(icia|ejandro|\ Pacino)')  # el | es un OR
coincidencias = patron.findall(texto)
for i in coincidencias:
    print('AL' + i)
