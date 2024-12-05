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

def isValid(pages, rules):
    for i in range(len(pages)):
        for j in range(i + 1, len(pages)):
            if not follows_rules(pages[i], pages[j], rules):
                return False
    return True

def sort(pages, rules):
    for i in range(len(pages)):
        for j in range(0, len(pages) - i - 1):
            if not follows_rules(pages[j], pages[j + 1], rules):
                pages[j], pages[j + 1] = pages[j + 1], pages[j]
    return pages

r = 0

for page in page_numbers:
    if not isValid(page.copy(), rules):
        sorted_pages = sort(page.copy(), rules)
        r += sorted_pages[len(sorted_pages) // 2]

print(r)

