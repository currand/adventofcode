import os

part = 'a'
test = True

filedir = os.path.dirname(__file__)
day = filedir[-2:]
if test:
    infile = filedir + f'/test{day}{part}.txt'
else:
    infile = filedir + f'/day{day}{part}.txt'

lines = [x.strip() for x in open(infile, 'r')]

LIMITS = {'red': 12, 'blue': 14, 'green': 13}

def parse_game(game: str) -> dict:
    """_summary_

    Args:
        game (str): _description_

    Returns:
        dict: _description_
    """
    cubes = {'red': 0, 'blue': 0, 'green': 0}
    cubes['title'] = int(game.split(': ')[0].replace('Game ', ''))
    sets = game.split(': ')[1].split('; ')
    for cube_set in sets:
        if ',' in cube_set:
            for x in cube_set.split(', '):
                num, color = x.split()
                cubes[color] = max(cubes[color], int(num))
        else:
            num, color = cube_set.split()
            cubes[color] = max(cubes[color], int(num))
    
    return cubes

if __name__ == '__main__':
    possibles = []
    for game in lines:
        possible = True
        game = parse_game(game)
        for key in LIMITS.keys():
            if game[key] > LIMITS[key]:
                possible = False
                break
        
        if possible:
            possibles.append(game['title'])
    
    print(sum(possibles))
