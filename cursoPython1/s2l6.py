"""
numero = 0
while numero < 5:
    print('hola')
    numero += 1
"""
"""
# While
nombre = ''
while nombre != 'Sundungu':
    print('escribí tu nombre, Sundungu')
    nombre = input()
print('Gracias')
"""
"""
# While con If y break
nombre = ''
while True:
    print('escribí tu nombre, Sundungu')
    nombre = input()
    if nombre == 'Sundungu':
        break
print('Gracias')
"""
# While con continue
soto = 0
while soto < 5:
    soto += 1
    if soto == 3:
        continue
    print('soto es ' + str(soto))