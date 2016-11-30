"""
import sys

print('hola')
sys.exit()
print('chau')
"""
import pyperclip

pyperclip.copy('hola')
print(pyperclip.paste())
