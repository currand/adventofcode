import os
from typing import Generator, List, Union, Iterator

def get_column(arr: list[list[int]], c: int) -> list:
    return [row[c] for row in arr]

def circle_grid(arr: list[list[int]], h: int, w: int,
                remove_corners: bool = False) -> Generator:
    """
    Return a generator that yields x,y coordinates
    circling the outside of a 2d grid from 0,0
    in the top left moving clockwise

    Args:
        arr (list): _description_
        h (int): _description_
        w (int): _description_

    Returns:
        Iterable: _description_
    """
    coords: list[tuple[int, int]] =  []
    coords += [(0, c) for c in range(1, w+1)]
    coords += [(h, c) for c in range (w, -1, -1)]
    coords += [(0, c) for c in range (w, -1, -1)]

    if remove_corners:
        coords = [x for x in coords if x not in get_corners(arr, h, w)]
    
    yield [item for item in coords]

def get_corners(arr: list[list[int]], h: int, w: int) -> list[tuple[int, int]]:
    return [(0,0), (0, w), (h, w), (h, 0)]

def side(h: int, w: int, coord: tuple[int, int]) -> str | None:
    if coord[0] == 0:
        return "TOP"
    elif coord[0] == h:
        return "BOTTOM"
    elif coord[1] == 0:
        return "LEFT"
    elif coord[1] == w:
        return "RIGHT"
    else:
        return None


if __name__ == '__main__':
    filedir = os.path.dirname(__file__)
    day = filedir[-2:]
    infile = filedir + f'/day{day}.txt'
    testfile = filedir + f'/test{day}.txt'
    lines = [x.strip() for x in open(testfile)]

    forrest = [[int(j) for j in i] for i in [list(line) for line in lines]]
    w = len(forrest[0])
    h = len(forrest)

    for tree in circle_grid(forrest, h, w, remove_corners=True):
        ''' 
        1. start from top left
        2. move clockwise using circle_crid()
        3. at each step
            1. If side() = TOP, get column, count trees taller than item 0
            2. If side() = RIGHT, get row, count trees (in reverse order) taller than item -1
            3. If side() = BOTTOM, get column, count trees taller than item -1 in reverse order
            4. If side() = LEFT, get row, count trees taller than item 0
        '''
        if side(h, w, tree) == 'TOP':
            column = get_column(forrest, tree(1))
        elif side(h, w, tree) == 'RIGHT':
            pass
        elif side(h, w, tree) == 'BOTTOM':
            pass
        elif side(h, w, tree) == 'LEFT':
            pass
    pass