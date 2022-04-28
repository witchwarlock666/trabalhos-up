# Fabricio Bertoncello Filho e Felipe Lacerda

import itertools
from operator import truediv
from random import randint

def findsubsets(s, n): 
    return list(itertools.combinations(s, n)) 
s = {1, 2, 3} 
n = 2

conjunto1 = [1, 2, 3, 4, 5]
conjunto2 = ["a", "b", "c", "d", "e"]
print("1)")
for c1 in conjunto1:
    for c2 in conjunto2:
        str(c1)
        print ("[{}, {}]\n".format(c1, c2))

i = 0
print("\n2) 1)\n")
while (i <= len(conjunto1)):
    print(findsubsets(conjunto1, i))
    i += 1

i = 0
print("\n2) 2)\n")
while (i <= len(conjunto2)):
    print(findsubsets(conjunto2, i))
    i += 1

conjunto3 = [1, 2, 3]

sub = findsubsets(conjunto3, 2)

subs = [sub[0], sub[2]]

print("\n5)\n")
print(subs)

print("\n6)")
print("\n111\n")
print("010\n")
print("100\n")
print("001\n")

print("7)\n")
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
