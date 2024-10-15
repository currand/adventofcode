import os

TEST = True

filedir = os.path.dirname(__file__)
part = __file__.split('.', maxsplit=1)[0][-1]
day = filedir[-2:]
if TEST:
    infile = filedir + f'/test{day}{part}.txt'
else:
    infile = filedir + f'/day{day}{part}.txt'

lines = [x.strip() for x in open(infile, 'r')]

def build_grid(data: list[str]) -> list[list[str]]:
    return [list(line) for line in data]

def is_symbol(char: str) -> bool:
    if '.' in char:
        return False
    elif char.isdigit():
        return False
    elif char == '':
        return False
    else:
        return True

def symbol_near(grid: list[list[str]], positions: list[tuple[int, int]]) -> bool:
    try:
        for pos in positions:
            for x in range(-1,2):
                for y in range(-1,2):
                    if (x,y) != (0,0) and pos[0]+x >=0 and pos[1]+y >= 0:
                        symbol = is_symbol(grid[pos[0]+x][pos[1]+y])
                        print(f'{grid[pos[0]+x][pos[1]+y]}: {symbol}')
    except IndexError:
        pass




if __name__ == '__main__':
    grid = build_grid(lines)
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char != '.':
                if char.isdigit():
                    symbol_near(grid, [(x,y)])


    
    pass
