"""
def div42(divisor):
    try:
        return 42 / divisor
    except ZeroDivisionError:
        print('error de división por cero')

print(div42(2))
print(div42(12))
print(div42(0))
print(div42(1))
"""

print('cuántos gatos tenés?')
nGatos = input()
try:
    if int(nGatos) >= 4:
        print('cuántos gatos!')
    elif int(nGatos) < 0:
        print('eso es imposible!')
    else:
        print('qué poquitos!')
except ValueError:
    print('con números, bestia!')
