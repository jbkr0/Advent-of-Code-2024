r = 0

def increasing(liste):
    return all(liste[i] < liste[i + 1] and liste[i + 1] - liste[i] <= 3 for i in range(len(liste) - 1))

def decreasing(liste):
    return all(liste[i] > liste[i + 1] and liste[i] - liste[i + 1] <= 3 for i in range(len(liste) - 1))

def safe(liste):
    for i in range(len(liste)):
        new_list = liste[:i] + liste[i+1:]
        if increasing(new_list) or decreasing(new_list):
            return True
    return False

with open('input.txt', 'r') as fichier:
    ligne = fichier.readline()
    while ligne:
        tmp = ligne.split()
        if increasing([int(x) for x in tmp]) or decreasing([int(x) for x in tmp]) or safe([int(x) for x in tmp]):
            r += 1
        ligne = fichier.readline()

print(r)