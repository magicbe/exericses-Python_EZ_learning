
lines = []
with open('3.txt', 'r', encoding='UTF-8-SIG') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split()
    time = s[0][:5]
    name = s[0][5:]
    print(name)