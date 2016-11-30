import pyperclip

aaa = ' - '.join(['a', 'b', 'c'])
print(aaa)

print('La sarlanga'.replace(' ', '').isalpha())
bbb = 'hola, cómo te va'.split()
print(bbb)
print('hola'.rjust(20, '*'))
print(aaa.strip('a'))  # saca los caracteres del principio y el final de la cadena
#copiar y pegar del portapapeles
pyperclip.copy('sarasaaaaaaa')
print(pyperclip.paste)
