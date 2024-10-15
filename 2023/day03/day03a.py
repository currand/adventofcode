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

def symbol_near(positions: list[tuple[int, int]]) -> bool:
    try:
        for pos in positions:
            for x_add in range(-1,2):
                for y_add in range(-1,2):
                    if (
                        (x_add,y_add) != (0,0)
                        and (pos[1]+y_add >=0 and pos[0]+x_add >= 0)
                        and (pos[1]+y_add <= len(grid[pos[1]])-1)
                        and (pos[0]+x_add <= len(grid[pos[0]])-1)
                        and is_symbol(grid[pos[1]+y_add][pos[0]+x_add])
                    ):
                        return True

    except IndexError:
        pass
    
    return False

def get_digits(pos: tuple[int,int]):
    positions = [pos]
    for x_add in range(1, len(grid[pos[1]])-pos[0]):
        if grid[pos[1]][pos[0]+x_add].isdigit():
            positions.append((pos[0]+x_add, pos[1]))
        else:
            break

    return positions

if __name__ == '__main__':
    grid = build_grid(lines)
    parts = []
    for y, line in enumerate(grid):
        X = 0
        if y == 139:
            pass
        while X <= len(line)-1:
            if line[X] != '.':
                if line[X].isdigit():
                    digits = get_digits((X,y))
                    if symbol_near(digits):
                        num = int(''.join([grid[x[1]][x[0]] for x in digits]))
                        parts.append(num)
                    X = digits[-1][0] + 1
                else:
                    X += 1
            else:
                X += 1

    print(sum(parts))
