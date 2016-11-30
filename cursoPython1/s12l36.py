import logging

# Configuración del módulo logging
# loguear a la stdout
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# loguear a un archivo
# logging.basicConfig(filename='s12l36.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

'''
#Programa sin logging
def factorial(numero):
    total = 1
    for i in range(numero + 1):
        total *= i
    return total
'''

# Programa con logging

# logging.disable(logging.CRITICAL)  # Con esto se deshabilitan los logs de CRITICAL para abajo

logging.debug('Comienzo')


def factorial(numero):
    logging.debug('Función factorial, numero es %s' % (numero))
    total = 1
    for i in range(1, numero + 1):
        total *= i
        logging.debug('i es %s. total es %s' % (i, total))
    logging.debug('Retora un total de %s' % (total))
    return total


print(factorial(6))

logging.debug('Final')
