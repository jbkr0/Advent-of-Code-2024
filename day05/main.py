import re

rules = []
page_numbers = []

with open('input.txt', 'r') as fichier:
    for line in fichier:
        line = line.strip()
        if not line:
            continue

        match = re.search(r"(\d+)\|(\d+)", line)
        if match:
            rules.append((int(match.group(1)), int(match.group(2))))
        if re.match(r'^\d+(?:,\d+)*$', line.strip()):
            page_numbers.append([int(x) for x in line.strip().split(',')])

def follows_rules(page1, page2, rules):
    if (page1, page2) in rules:
        return True
    if (page2, page1) in rules:
        return False
    return True

r = 0

for page in page_numbers:
    valid = True

    for i in range(len(page)):
        for j in range(i + 1, len(page)):
            if not follows_rules(page[i], page[j], rules):
                valid = False
                break
        if not valid:
            break
    if valid:
        r += page[len(page)//2]

print(r)

