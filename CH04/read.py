# 讀取檔案

data = []
with open('./CH04/food.txt', 'r') as f:
    for line in f:
        data.append(line.strip())

print(data)