import os

filedir = os.path.dirname(__file__)
day = filedir[-2:]
infile = filedir + f'/day{day}.txt'
testfile = filedir + f'/test{day}.txt'
lines = [x.strip() for x in open(infile)]

subsets = 0
for line in lines:
    a, b, x, y = map(int, line.replace(",", "-").split("-"))
    if set(range(a, b + 1)) & set(range(x, y + 1)):
        subsets += 1
    
print(subsets)