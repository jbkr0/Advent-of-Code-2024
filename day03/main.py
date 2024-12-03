import re

pattern = r'mul\((\d+),(\d+)\)'
pattern_do = r'do\(\)'
pattern_dont = r"don't\(\)"

r = 0
b = True

with open('input.txt', 'r') as fichier:
    ligne = fichier.readline()
    while ligne:
        tokens = re.split(r'(\bdo\(\)|\bdon\'t\(\)|mul\(\d+,\d+\))', ligne.strip())
    
        for token in tokens:
            if re.match(pattern_do, token):
                b = True
            elif re.match(pattern_dont, token):
                b = False
            elif re.match(pattern, token) and b:
                match = re.match(pattern, token)
                num1 = int(match.group(1))
                num2 = int(match.group(2))
                r += num1 * num2
        ligne = fichier.readline()

print(r)