#  CCF : LOTO #
from random import *

grille = [7, 13, 20, 33, 47, 49]

tirage = [0, 0, 0, 0, 0, 0]

def test(n, tab):
    resu = False
    i = 0
    while (i<6) and resu==False:
        if n == tab[i]:
            resu = True
        i = i+1
    return resu


compt = 0
while compt < 6:
    num = randint(1,49)  # nombre aléatoire entre 1 et 49
    if test(num, tirage)== False:
        tirage[compt] = num
        compt = compt+1
print(tirage)
