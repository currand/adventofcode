import os
from pprint import pp
from typing import Generator, List, Union, Iterator

class Grid():
    def __init__(self, arr: list[list[int]]) -> None:
        self.w = len(arr[0]) - 1
        self.h = len(arr) - 1
        self.grid = arr
    
    def __repr__(self) -> str | None:
        pp(self.grid)

    def set_coord(self, r: int, c: int, data: int) -> None:
        self.grid[r][c] = data

    def get_coord(self, r: int, c: int) -> int | None:
        return self.grid[r][c]

    def get_column(self, c: int) -> list[tuple[int,int,int]]:
        out: list[tuple[int,int,int]] = []
        for i,r in enumerate(self.grid):
            out.append((i, c, self.grid[i][c]))
        return out

    def get_row(self, r: int):
        return [(r, c, self.grid[r][c]) for c in range(0,len(self.grid[r]))]

    def circle_grid(self, remove_corners: bool = False) -> Generator:
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
        coords += [(0, c) for c in range(1, self.w+1)]
        coords += [(r, self.w) for r in range(1, self.h+1)]
        coords += [(self.h, c) for c in range (self.w, -1, -1)]
        coords += [(0, r) for r in range (self.h, -1, -1)]

        if remove_corners:
            coords = [x for x in coords if x not in self.get_corners()]
        
        for item in coords:
            yield item

    def get_corners(self) -> list[tuple[int, int]]:
        return [(0,0), (0, self.w), (self.h, self.w), (self.h, 0)]

def side(grid, coord: tuple[int, int]) -> str | None:
    if coord[0] == 0:
        return "TOP"
    elif coord[0] == grid.h:
        return "BOTTOM"
    elif coord[1] == 0:
        return "LEFT"
    elif coord[1] == grid.w:
        return "RIGHT"
    else:
        return None

def count_trees(arr: list[tuple[int, int, int]]) -> list[int]:
    tall_trees = []
    curr_min = arr.pop(0)[2]
    for coord in arr[:-1]:
        if coord[2] > curr_min:
            tall_trees.append((coord[0], coord[1]))
            curr_min = coord[2]
    
    return tall_trees

if __name__ == '__main__':
    filedir = os.path.dirname(__file__)
    day = filedir[-2:]
    infile = filedir + f'/day{day}.txt'
    testfile = filedir + f'/test{day}.txt'
    lines = [x.strip() for x in open(infile)]

    forrest = [[int(j) for j in i] for i in [list(line) for line in lines]]
    grid = Grid(forrest)

    trees = []
    outside = 4
    for tree in grid.circle_grid(remove_corners=True):
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
        if side(grid, tree) == 'TOP':
            column = grid.get_column(tree[1])
            trees += count_trees(column)
        elif side(grid, tree) == 'RIGHT':
            row = grid.get_row(tree[0])
            trees  += count_trees(row[::-1])
        elif side(grid, tree) == 'BOTTOM':
            column = grid.get_column(tree[1])
            trees  += count_trees(column[::-1])
        elif side(grid, tree) == 'LEFT':
            row = grid.get_row(tree[0])
            trees  += count_trees(row)
    
    
    print('trees: {}, outside: {}, {}'.format(len(set(trees)), outside, len(set(trees)) + outside))
    pass