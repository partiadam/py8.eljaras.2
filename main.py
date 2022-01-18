'''
2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!
'''

def parameter_eldonto_szamos(tipus):
    if tipus < 0:
        print('Negatív érték.')
    if tipus == 0:
        print('Az érték nulla.')
    if tipus > 0:
        print('Pozitív érték.')

parameter_eldonto_szamos(-1)
