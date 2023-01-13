from utils.utils import get_input

lines = get_input('day3.txt')

alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
p = dict(zip(alph, range(1,53)))

sacks = []
for line in lines:
    length = (len(line) // 2)
    sacks.append(({x for x in line[:length]}, {x for x in line[length:]}))

total = 0
for sack in sacks:
    total += p[list(sack[0].intersection(sack[1]))[0]]


print(total)