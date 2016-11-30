import re

empieza = re.compile(r'^Hola')  # afuera de  los [], el ^ significa "al principio de la linea"
print(empieza.search('Hola, che'))
print(empieza.search('¡Hola, che!'))

termina = re.compile(r'che$')  # el $ significa "al final de la linea"
print(termina.search('Hola, che'))
print(termina.search('¡Hola, che!'))

unregex = re.compile(r'.ato')  # el . significa "cualquier caracter"
print(unregex.findall('pato, gato, mato'))

texto = 'Nombre: Roberte Apellido: Garzullo'
nombreRe = re.compile(r'Nombre: (.*) Apellido: (.*)')  # .* significa "cero o más de lo que sea"

print(nombreRe.findall(texto))
milista = nombreRe.findall(texto)
print(milista[0][1])

texto2 = '<te quiero> matar> lalalalala.'
ngreRe = re.compile(r'<(.*?)>')  # non-greedy con ?
greRe = re.compile(r'<(.*)>')  # greedy
print(ngreRe.findall(texto2))
print(greRe.findall(texto2))
texto3 = 'LAlala\nSEsese\nTOtoto'
dotallRe = re.compile(r'.*', re.DOTALL)  # con esto el . también incluye \n
print(dotallRe.search(texto3))
dotiRe = re.compile(r'[aeiou]', re.I)  # con esto el re.compile ignora el Case
print(dotiRe.findall(texto3))
