from utils.utils import get_input

line = get_input('day6.txt')[0]

for i in range(14, len(line)):
    check = line[i-14:i]
    if len(set(check)) == len(check):
        print(i)
        break