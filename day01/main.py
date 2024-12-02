l1 = []
l2 = []

with open('input.txt', 'r') as fichier:
    ligne = fichier.readline()
    while ligne:
        tmp = ligne.split()
        l1.append(int(tmp[0]))
        l2.append(int(tmp[1]))
        ligne = fichier.readline()

l1.sort()
l2.sort()

r = 0

for a,b in zip(l1,l2):
    if a < b:
        r += b-a
    else:
        r += a-b

print(r)