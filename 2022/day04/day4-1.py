import os

filedir = os.path.dirname(__file__)
day = filedir[-2:]
infile = filedir + f'/day{day}.txt'
testfile = filedir + f'/test{day}.txt'
lines = [x.strip() for x in open(infile)]

subsets = 0
for line in lines:
    a = line.split(',')
    b = [int(x) for x in a[0].split('-')]
    c = [int(x) for x in a[1].split('-')]
    first = set(range(b[0], b[1]+1))
    second = set(range(c[0], c[1]+1))

    if first.issubset(second) or second.issubset(first):
        subsets += 1
    
print(subsets)