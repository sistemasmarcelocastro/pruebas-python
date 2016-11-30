import requests
'''
respuesta = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(respuesta.status_code)  # el status code 200 significa ok
print(len(respuesta.text))
print(respuesta.text[:200])  # el .text contiene lo que se descargó

print(respuesta.raise_for_status())
'''
respuesta2 = requests.get('https://automasdsdtetheboringstuff.com/files/rj.txt')
respuesta2.raise_for_status()
print('hola')