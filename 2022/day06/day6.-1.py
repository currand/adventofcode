import os

filedir = os.path.dirname(__file__)
day = filedir[-2:]
infile = filedir + f'/day{day}.txt'
testfile = filedir + f'/test{day}.txt'
lines = [x.strip() for x in open(infile)]
line = lines[0]

for i in range(4, len(line)):
    check = line[i-4:i]
    if len(set(check)) == len(check):
        print(i)
        break


pass