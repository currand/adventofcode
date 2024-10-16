import os
from functools import reduce

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

def number_near(pos: tuple[int, int]) -> list[tuple[int,int]] | None:

    numbers = []
    for x_add in range(-1,2):
        for y_add in range(-1,2):
            if (
                (x_add,y_add) != (0,0)
                and (pos[1]+y_add >=0 and pos[0]+x_add >= 0)
                and (pos[1]+y_add <= len(grid[pos[1]])-1)
                and (pos[0]+x_add <= len(grid[pos[0]])-1)
                and grid[pos[1]+y_add][pos[0]+x_add].isdigit()
            ):
                numbers.append((pos[0]+x_add, pos[1]+y_add))
                continue

    if len(numbers) > 0:
        return numbers
    else:
        return None

def get_digits(coords: list[tuple[int,int]]):
    final_digits = []
    coords_seen = []
    for coord in coords:
        if coord in coords_seen:
            continue

        y = coord[1]
        x = coord[0] - 1
        min_x = 0
        max_x = len(grid[y])-1
        curr_digits = [grid[y][x+1]]
        # Look backward until a non digit
        while x >= min_x:
            coords_seen.append((x,y))
            if grid[y][x].isdigit():
                curr_digits.insert(0, grid[y][x])
            else:
                break
            x -= 1
        
        x = coord[0] + 1
        while x <= max_x:
            coords_seen.append((x,y))
            if grid[y][x].isdigit():
                curr_digits.append(grid[y][x])
            else:
                break
            x += 1
        
        final_digits.append(curr_digits)

    return final_digits

if __name__ == '__main__':
    grid = build_grid(lines)
    parts = []
    for y, line in enumerate(grid):
        X = 0
        if y == 5:
            pass
        while X <= len(line)-1:
            if line[X] == '*':
                if positions := number_near((X,y)):
                    digits = get_digits(positions)
                    if len(digits) == 2:
                        parts.append(reduce(lambda x, y: int(''.join(x)) * int(''.join(y)), digits))
                    else:
                        pass
            X += 1

    print(sum(parts))
