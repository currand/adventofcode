import os
from pprint import pp
from typing import Generator, List, Union, Iterator

class Grid():
    def __init__(self, h: int, w: int) -> None:
        self.grid = [[None for c in range(0, w)] for r in range(0, h)]
    
    def __repr__(self) -> str:
        pp(self.grid)

    def add_coord(self, r: int, c: int, data: int) -> None:
        self.grid[r][c] = data

    def get_coord(self, r: int, c: int) -> int:
        return self.grid[r][c]

    def get_column(self, c: int):
        return {(row, col[c]) for row, col in enumerate(self.grid)

def get_column(arr: list[list[int]], c: int) -> list:
    return [(row, col[c]) for row, col in enumerate(arr)]

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
    coords += [(r, w) for r in range(1, h+1)]
    coords += [(h, c) for c in range (w, -1, -1)]
    coords += [(0, r) for r in range (h, -1, -1)]

    if remove_corners:
        coords = [x for x in coords if x not in get_corners(arr, h, w)]
    
    for item in coords:
        yield item

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

def count_trees(arr: list[tuple[int, int]], how: str) -> list[int]:
    tall_trees = []
    if how == 'r':
        curr_min = arr.pop(0)[0]
        for coord in arr[:-1]:
            if coord[0] > curr_min:
                tall_trees.append(coord)
                curr_min = coord[0]
    else:
        curr_min = arr.pop(0)[1]
        for coord in arr[:-1]:
            if coord[1] > curr_min:
                tall_trees.append(coord)
                curr_min = coord[1]
    
    return tall_trees


if __name__ == '__main__':
    filedir = os.path.dirname(__file__)
    day = filedir[-2:]
    infile = filedir + f'/day{day}.txt'
    testfile = filedir + f'/test{day}.txt'
    lines = [x.strip() for x in open(testfile)]

    forrest = [[int(j) for j in i] for i in [list(line) for line in lines]]
    w = len(forrest[0]) - 1
    h = len(forrest) - 1
    trees = []
    outside = 4
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

        outside += 1
        if side(h, w, tree) == 'TOP':
            column = get_column(forrest, tree[1])
            trees += count_trees(column, 'c')
        elif side(h, w, tree) == 'RIGHT':
            row = [(tree[0], c) for c in forrest[tree[0]:-1]]
            count  += count_trees(row[-2:0:-1], min_h=row[-1])
        elif side(h, w, tree) == 'BOTTOM':
            column = get_column(forrest, tree[1])
            count  += count_trees(column[-1:1:-1], min_h=column[-1])
        elif side(h, w, tree) == 'LEFT':
            row = forrest[tree[0]]
            count  += count_trees(row[1:], min_h=row[0])
        
    print(count + outside)
    pass