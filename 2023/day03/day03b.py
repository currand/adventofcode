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

    if len(numbers) > 0:
        return numbers
    else:
        return None

def get_digits(coords: list[tuple[int,int]]):
    final_digits = []
    for coord in coords:
        Y = coord[1]
        X = coord[0]
        min_x = 0
        max_x = len(grid[Y]) - 1
        curr_digits = [grid[Y][X]]
        # Look backward until a non digit
        while X >= min_x:
            if grid[Y][X-1].isdigit():
                curr_digits.insert(0, grid[Y][X-1])
            X -= 1
        
        X = coord[0]
        while X <= max_x:
            if grid[Y][X-1].isdigit():
                curr_digits.append(grid[Y][X-1])
            X += 1


    return positions

if __name__ == '__main__':
    grid = build_grid(lines)
    parts = []
    for y, line in enumerate(grid):
        X = 0
        if y == 139:
            pass
        while X <= len(line)-1:
            if line[X] == '*':
                if positions := number_near((X,y)):
                    digits = get_digits(positions)
            else:
                X += 1

    print(sum(parts))
