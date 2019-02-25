with open('input.txt', 'r', encoding='UTF-8_sig') as f:
    name = ''
    data = ''
    for line in f:
        if line.strip() == 'Allen':
            name = 'Allen'
        elif line.strip() == 'Tom':
            name = 'Tom'
        else:
            data = data + name + ': ' + line

with open('output.txt', 'w', encoding='UTF-8') as f:
    f.write(data)