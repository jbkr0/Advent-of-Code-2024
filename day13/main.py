import re
import pulp

with open('input.txt', 'r') as fichier:
    file = fichier.read()

regex = r"Button (\w): X([+-]?\d+), Y([+-]?\d+)|Prize: X=(\d+), Y=(\d+)"

matches = re.findall(regex, file)

claw_machines = []
claw_machine = []

for match in matches:
    if match[0]:
        claw_machine.append((int(match[1]), int(match[2])))
    else:
        claw_machine.append((int(match[3]), int(match[4])))
        claw_machines.append(claw_machine)
        claw_machine = []

r = 0

for eq in claw_machines:
    prob = pulp.LpProblem("Minimize_Weight", pulp.LpMinimize)

    a = pulp.LpVariable('a', lowBound=0, cat='Integer')
    b = pulp.LpVariable('b', lowBound=0, cat='Integer')

    prob += 3 * a + b

    prob += eq[0][0] * a + eq[1][0] * b == eq[2][0]
    prob += eq[0][1] * a + eq[1][1] * b == eq[2][1]

    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    if pulp.LpStatus[prob.status] != 'Optimal':
        continue

    a_value = pulp.value(a)
    b_value = pulp.value(b)
    r += 3 * a_value + b_value

print(r)