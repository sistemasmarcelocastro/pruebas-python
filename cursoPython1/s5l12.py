# Juego: adivinar un número
import random

print('Hola, cómo te llamás?')
nombre = input()
print('Bueno, ' + nombre + ', estoy pensando en un número del 1 al 20')
secreto = random.randint(1, 20)
for intentos in range(1, 7):
    print('adiviná')
    entrada = int(input())
    if entrada < secreto:
        print('muy bajo...')
    elif entrada > secreto:
        print('muy alto...')
    else:
        break  # esto es si adivinó.
# print('Eeessssaaa, adivinadorrr!')

if entrada == secreto:
    print('Eeessssaaa, adivinadorrr!')
    print('lo lograste en ' + str(intentos) + ' intentos')
else:
    print('no, no, el número era ' + str(secreto) + ', salame!')
