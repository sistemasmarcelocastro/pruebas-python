import shutil

shutil.copy('hola2.txt', '.\\directorio1\\hola2_copia.txt')
shutil.copytree('.\\directorio1', '.\\directorio1_copia')
shutil.move('.\\directorio1_copia\\hola2_copia.txt','.\\')