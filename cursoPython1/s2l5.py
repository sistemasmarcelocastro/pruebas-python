"""
nombre = 'Surlanga'
if nombre == 'Surlanga':
    print('Hola, Surlanga')
print('Listo')

password = 'besugo'
if password == 'besugo':
    print('acceso concedido')
else:
    print('errooooooorrrr!!!!!!!!')
"""

# La estructura IF-ELIF solo ejecuta el primer condicional verdadero que encuentra
nombre = 'Pedro'
edad = 3000
if nombre == 'Pablo':
    print('Hola, Pablo')
elif edad < 20:
    print('Volá de acá, pendejo!')
elif edad > 2000:
    print('Por qué no estás muerto?')
elif edad > 100:
    print('Vos no sos Pablo, viejo choto')
