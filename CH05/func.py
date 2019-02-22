# function 函式/功能

# function 是用來【收納】程式碼的
# 它是個功能

def wash(dry=False, water=8):
    print('加水', water, '分滿')
    print('加洗衣精')
    print('旋轉')
    if dry:
        print('烘衣')

wash(water=10) # 使用 function

def say_hi():
    print('hi!')

say_hi()

def add(x=1, y=2):
    return x + y

print(add(5))
print(add(y=5))

result = add(3, 4)
print(result)

def average(numbers):
    return sum(numbers) / len(numbers)

print(average([1, 2, 3]))
print(average([23, 32, 6]))
print(average([180, 34, 92]))