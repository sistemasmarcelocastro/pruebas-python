import os

for direc, subdirec, archivos in os.walk('C:\\Users\\Damián\\PycharmProjects'):
    print('Directorio: ' + direc)
    print('Subdirectorios: ' + str(subdirec))
    print('Archivos: ' + str(archivos))
    print('\n')
