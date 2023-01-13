from utils.utils import get_input

lines = get_input('test4.txt')

subsets = 0
for line in lines:
    a, b, x, y = map(int, line.replace(",", "-").split("-"))
    if set(range(a, b + 1)) & set(range(x, y + 1)):
        subsets += 1
    
print(subsets)