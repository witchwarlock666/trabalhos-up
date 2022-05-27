# Fabricio Bertoncello Filho e Felipe Lacerda

import itertools
from operator import truediv
from random import randint

def findsubsets(s, n): 
    return list(itertools.combinations(s, n)) 
s = {1, 2, 3} 
n = 2

#ex 1
conjunto1 = [1, 2, 3, 4, 5]
conjunto2 = ["a", "b", "c", "d", "e"]

#ex 2
for c1 in conjunto1:
    for c2 in conjunto2:
        str(c1)
        print ("[{}, {}]\n".format(c1, c2))

#ex 3
i = 0
while (i <= len(conjunto1)):
    print(findsubsets(conjunto1, i))
    i += 1

i = 0
while (i <= len(conjunto2)):
    print(findsubsets(conjunto2, i))
    i += 1

#ex 4
conjunto3 = [1, 2, 3, 4]

#ex 5

sub = findsubsets(conjunto3, 2)

subs = [sub[0], sub[2]]

#ex 6
print(subs)

print("\n1101\n")
print("1000\n")
print("0100\n")
print("0011\n")

#ex 7
n = 5
resultados = [None, None, None, None, None]
x = 0
cont = True
while (cont):
    count = 0
    f = x * 2
    resultados[x] = f
    inj = True
    for item in resultados:
        if (resultados[x] == item):
            count += 1
            if (count > 1):
                print("Não injetora")
                inj = False
                cont = False
    x += 1
    if (x > 4):
        cont = False

if (inj):
    print("Injetora")

print("Aperte enter para finalizar: ")
input()
