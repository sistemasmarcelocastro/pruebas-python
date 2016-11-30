#! python3

'''Este prgrama toma lo que hay en el portapapeles,
encuentra teléfonos y emails
y los copia otra vez al portapapeles.'''

import re, pyperclip

# crear regex para telefonos
telRe = re.compile(r'''
# Formatos posibles: 123-456-7890, 123-4567, (123) 456-7890, 123-4567 ext 12345, 123-4567 ext. x12345
(
((\d\d\d)|\(\d\d\d\))?          # códifgo de area (opcional)
(\s|-)                          # primer separador
\d\d\d                          # primeros 3 digitos
-                               # segundo separador
\d\d\d\d                        # últimos 4 digitos
(((ext(\.)?\s)|x)               # extnsión - letras (opcional)
(\d{2,5}))?                     # extnsión - numero (opcional)
)                               # este es el grupo 0, para que el findall no devuelva tuplas separadas
''', re.VERBOSE)  # elverbose permite la multilinea con los '''

# crear regex para emails
mailRe = re.compile(r'''
#formato: algo.+_@algo.algo
[a-zA-Z_+.]+                     #nombre
@                                #at
[a-zA-Z_+.]+                     #dominio
''', re.VERBOSE)

# obtenet texto del portapapeles
texto = pyperclip.paste()

# extraer emails y tels del texto
listaTels = telRe.findall(texto)
listaMails = mailRe.findall(texto)

soloTels = []
for numero in listaTels:  # numero se llena con cada tupla de listaTels
    soloTels.append(numero[0])  # solo agrega el elemento 0 de cada tupla

print(soloTels)
print(listaMails)

# copiar lo extraido al portapapeles
todoJunto = '\n'.join(soloTels) + '\n' + '\n'.join(listaMails)
pyperclip.copy(todoJunto)
