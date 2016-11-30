import webbrowser, sys, pyperclip

# webbrowser.open('https://www.youtube.com/')  # Abre la url en un navegador


### Este programa toma una dirección y la busca en google maps:
# Comprobar si hay argumentos:
if len(sys.argv) > 1:
    direccion = ' '.join(sys.argv[1:])
else:
    direccion = pyperclip.paste()

webbrowser.open('https://www.google.com.ar/maps/place/%s' % (direccion))
