import os

filedir = os.path.dirname(__file__)
day = filedir[-2:]
infile = filedir + f'/day{day}a.txt'
testfile = filedir + f'/test{day}a.txt'
lines = [x.strip() for x in open(infile)]

LIMITS = {'red': 12, 'blue': 13, 'green': 14}

def parse_game(line):
    cubes = {'red': 0, 'blue': 0, 'green': 0}
    cubes['title'] = int(line.split(': ')[0].replace('Game ', ''))
    sets = line.split(': ')[1].split('; ')
    for set in sets:
        if ',' in set:
            for x in set.split(', '):
                num, color = x.split()
                cubes[color] = max(cubes[color], int(num))
        else:
            num, color = set.split()
            cubes[color] = max(cubes[color], int(num))
    
    return cubes

if __name__ == '__main__':
    possibles = []
    for line in lines:
        possible = True
        game = parse_game(line)
        for key in LIMITS.keys():
            if game[key] > LIMITS[key]:
                possible = False
                break
        
        if possible:
            possibles.append(game['title'])
    
    print(sum(possibles))
