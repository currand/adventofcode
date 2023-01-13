from utils.utils import get_input

lines = get_input('test4.txt')

subsets = 0
for line in lines:
    a = line.split(',')
    b = [int(x) for x in a[0].split('-')]
    c = [int(x) for x in a[1].split('-')]
    first = set(range(b[0], b[1]+1))
    second = set(range(c[0], c[1]+1))
    
    if any([True for x in first if x in second]):
        subsets += 1
    
print(subsets)