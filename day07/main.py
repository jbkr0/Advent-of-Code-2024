import re

equList = []

with open('input.txt', 'r') as fichier:
    for line in fichier:
        match = re.match(r"^(\d+): ((?:\d+ *)+)$", line.strip())
        if match:
            equList.append((int(match.group(1)), [int(x) for x in match.group(2).split()]))

def eval(nbList, ops):
    r = nbList[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            r += nbList[i + 1]
        else:
            r *= nbList[i + 1]
    return r

r = 0

for eq in equList:
    nbList = eq[1]
    nb_ops = len(nbList) - 1

    for i in range(2**nb_ops):
        ops = []
        for j in range(nb_ops):
            ops.append('+' if (i >> j) & 1 else '*')
        result = eval(nbList, ops)
        if result == eq[0]:
            r += eq[0]
            break


print(r)
