import re

texto = 'el Agente Soto encontró los documentos del Agente Tito'
nombresRe = re.compile(r'Agente \w+')
print(nombresRe.findall(texto))
print(nombresRe.sub('--SECRETO--', texto))  # Replace
nombresRe2 = re.compile(r'Agente (\w)\w*')
print(nombresRe2.sub('Agente \1 ****', texto))  # el \1 refiere al 1er grupo de la regex


