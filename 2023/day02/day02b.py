import os

TEST = False

filedir = os.path.dirname(__file__)
part = __file__.split('.', maxsplit=1)[0][-1]
day = filedir[-2:]
if TEST:
    infile = filedir + f'/test{day}{part}.txt'
else:
    infile = filedir + f'/day{day}{part}.txt'

lines = [x.strip() for x in open(infile, 'r')]

LIMITS = {'red': 12, 'blue': 14, 'green': 13}

def parse_game(game: str) -> int:
    """_summary_

    Args:
        game (str): _description_

    Returns:
        int: _description_
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
    
    return cubes['red'] * cubes['blue'] * cubes['green']

if __name__ == '__main__':
    powers = []
    for game in lines:
        powers.append(parse_game(game))
        
    
    print(sum(powers))
