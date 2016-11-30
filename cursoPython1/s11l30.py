import os

# print(os.path.join('c:','usr','bin'))" es OS agnostic
print(os.getcwd())
# os.chdir('c:\\')
print(os.getcwd())
print(os.path.isabs('c:\\'))
relativo = '..\\..\\'
absoluto = os.path.abspath(relativo)
print(absoluto)

rel2 = os.path.relpath('c:\\users\\Damián\\', 'c:\\')
print(rel2)
rel3 = os.path.relpath('c:\\', 'c:\\users\\Damián\\')
print(rel3)
directorio = os.path.dirname('c:\\users\\Damián\\petete.txt')  # solo el directorio
print(directorio)
archivo = os.path.basename('c:\\users\\Damián\\petete.txt')  # solo el archivo o el último directorio
print(archivo)
existe = os.path.exists('c:\\Users\\Damián\\')
print(existe)
print(os.path.isdir('c:\\Users\\Damián\\'))
print(os.path.isfile('c:\\Users\\Damián\\'))
print(os.path.getsize('c:\\windows\\system32\\calc.exe'))
print(os.listdir('c:\\users\\Damián\\'))


### Cuentael tamaño en MB de los archivos dentro de un dir (no recursivo)
def tamano(direc):
    total = 0
    for i in os.listdir(direc):
        absol = os.path.join(direc, i)
        if not os.path.isfile(absol):
            continue
        total += os.path.getsize(absol)
    totalMB = int(total) / 1024 / 1024
    return totalMB

print(tamano('c:\\Users\\Damián\\PycharmProjects\\cursoPython1\\'))

os.makedirs('c:\\SALAME\\CONQUESO')