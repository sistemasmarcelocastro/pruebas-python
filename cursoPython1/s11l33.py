import os, shutil

'''
peteteFile = open('petete.txt', 'w')
peteteFile.write('lalalalala\nlalalalala\nlalalalala')
peteteFile.close()
os.mkdir('.\\directorio')
shutil.move('petete.txt', '.\\directorio\\petete.txt')
shutil.copytree('.\\directorio', '.\\directorio2')

os.unlink('.\\directorio\\petete.txt')  # Borra archivos
os.rmdir('.\\directorio')  # Borra directorios si están vacíos
shutil.rmtree('.\\directorio2')  # Borra directorios y su contenido
'''
os.mkdir('.\\directorio')
os.chdir('.\\directorio')
for i in range(0, 10):
    peteteFile = open('petete' + str(i) + '.txt', 'w')
    peteteFile.write('lalalalala\nlalalalala\nlalalalala')
    peteteFile.close()

for archivo in os.listdir(): #devuelve una lista de strings con el contenido del cwd
    if str(archivo).endswith('.txt'):
        os.unlink(archivo)
        print(archivo)
os.chdir('..\\')
os.rmdir('.\\directorio')
