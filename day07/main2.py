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
        elif ops[i] == '*':
            r *= nbList[i + 1]
        else:
            r = int(str(r) + str(nbList[i + 1]))
    return r

def generate_ops(n, nb_ops):
    ops = []
    for _ in range(nb_ops):
        op = n % 3
        ops.append('+' if op == 0 else '*' if op == 1 else '||')
        n //= 3
    return ops

r = 0

for eq in equList:
    nbList = eq[1]
    nb_ops = len(nbList) - 1

    for i in range(3**nb_ops):
        ops = generate_ops(i, nb_ops)
        result = eval(nbList, ops)
        if result == eq[0]:
            r += eq[0]
            break

print(r)
