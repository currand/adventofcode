import os
from pprint import pp
from typing import Generator, List, Union, Iterator

class Grid():
    def __init__(self, arr: list[list[int]]) -> None:
        self.w = len(arr[0])
        self.h = len(arr)
        self.grid = arr
    
    def __repr__(self) -> str:
        pp(self.grid)

    def set_coord(self, r: int, c: int, data: int) -> None:
        self.grid[r][c] = data

    def get_coord(self, r: int, c: int) -> int:
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
        coords += [(0, c) for c in range(1, self.w)]
        coords += [(r, self.w-1) for r in range(1, self.h)]
        coords += [(self.h-1, c) for c in range (self.w-1, -1, -1)]
        coords += [(r, 0) for r in range (self.h-1, -1, -1)]

        if remove_corners:
            coords = [x for x in coords if x not in self.get_corners()]
        
        for item in coords:
            yield item

    def get_corners(self) -> list[tuple[int, int]]:
        return [(0,0), (0, self.w-1), (self.h-1, self.w-1), (self.h-1, 0)]

    def all_coords(self) -> Generator:
        coords = []
        for r in range(grid.h):
            if r not in [0,grid.h-1]:
                for c in range(0,grid.w):
                    if c not in [0,grid.w-1]:
                        coords.append((r, c, self.grid[r][c]))
        
        for item in coords:
            yield item

        

def side(grid, coord: tuple[int, int]) -> str | None:
    if coord[0] == 0:
        return "TOP"
    elif coord[1] == grid.w-1:
        return "RIGHT"
    elif coord[0] == grid.h-1 and coord[0] > 0:
        return "BOTTOM"
    elif coord[1] == 0:
        return "LEFT"

    else:
        return None

def count_trees(arr: list[tuple[int, int, int]]) -> list[int]:
    short_trees = []
    try:
        curr_min = arr.pop(0)[2]
        if arr[0][2] >= curr_min:
            return [(arr[0][0], arr[0][1])]

        for coord in arr:
            if coord[2] < curr_min:
                short_trees.append(coord)
            else:
                short_trees.append(coord)
                break

    except IndexError:
        short_trees = arr
    
    return short_trees

if __name__ == '__main__':
    filedir = os.path.dirname(__file__)
    day = filedir[-2:]
    infile = filedir + f'/day{day}.txt'
    testfile = filedir + f'/test{day}.txt'
    testfile2 = filedir + f'/test.txt'
    lines = [x.strip() for x in open(infile)]

    forrest = [[int(j) for j in i] for i in [list(line) for line in lines]]
    grid = Grid(forrest)

    high_score = 0
    for tree in grid.all_coords():
        ''' 
        1. start from top left
        2. move through all coords except the edges
        3. at each step
            1. look up
            2. count trees shorter than current tree
            3. repeat 1.1, 1.2 for each direction
        '''

        
        #  Look up
        column = grid.get_column(tree[1])[tree[0]::-1]
        u = count_trees(column)
        column = grid.get_column(tree[1])[tree[0]:]
        d = count_trees(column)
        row = grid.get_row(tree[0])[tree[1]::-1]
        l = count_trees(row)
        row = grid.get_row(tree[0])[tree[1]:]
        r = count_trees(row)
        total = len(u) * len(d) * len(l) * len(r)

        if total > high_score:
            high_score = total

        pass

    print(high_score)