from utils.utils import get_input

lines = get_input('day3.txt')

alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
p = dict(zip(alph, range(1,53)))

sacks = []
for i in range(0,len(lines), 3):
    sacks.append(({x for x in lines[i]}, {x for x in lines[i+1]}, {x for x in lines[i+2]}))

total = 0
for sack in sacks:
    total += p[list(sack[0].intersection(sack[1]).intersection(sack[2]))[0]]


print(total)