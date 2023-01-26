import os
from pprint import pp
from typing import Generator, List, Union, Any

class Grid():
    def __init__(self, arr: list[list[Any]]) -> None:
        self.w = len(arr[0])
        self.h = len(arr)
        self.grid = arr
        self.visited: list[tuple[int,int]] = []
        self._head_pos = (self.w // 2, self.h //2)
        self._tail_pos: self._head_pos

    def set_coord(self, r: int, c: int, data: Any) -> None:
        self.grid[r][c] = data

    def get_coord(self, r: int, c: int) -> Any:
        return self.grid[r][c]

    def update_pos(self, r, c) -> None:
        self._head_pos = (r, c)

    def move_right(self, i: int) -> None:
        self._head_pos = (self._head_pos[0], self._head_pos[1]+i)
        if self._head_pos[1] - self._tail_pos[1] >= 2:
            self._tail_pos[0] = self._head_pos[0]
            self._tail_pos[1] = self._head_pos[0] - 1
    
    def move_left(self, r: int, c: int) -> None:
        self._head_pos = (self._head_pos[0], self._head_pos[1]-1)
    
    def move_up(self, r: int, c: int) -> None:
        self._head_pos = (self._head_pos[0]+1, self._head_pos[1])

    def move_down(self, r: int, c: int) -> None:
        self._head_pos = (self._head_pos[0]-1, self._head_pos[1])

    def get_column(self, c: int) -> list[tuple[int,int,Any]]:
        out: list[tuple[int,int,int]] = []
        for i,r in enumerate(self.grid):
            out.append((i, c, self.grid[i][c]))
        return out

    def get_row(self, r: int):
        return [(r, c, self.grid[r][c]) for c in range(0,len(self.grid[r]))]

    def get_corners(self) -> list[tuple[int, int]]:
        return [(0,0), (0, self.w-1), (self.h-1, self.w-1), (self.h-1, 0)]

    def all_coords(self) -> Generator:
        for r in grid.h-1:
            for c in grid.w-1:
                yield (r, c, self.grid[r][c])


if __name__ == '__main__':
    filedir = os.path.dirname(__file__)
    day = filedir[-2:]
    infile = filedir + f'/day{day}.txt'
    testfile = filedir + f'/test{day}.txt'
    testfile2 = filedir + f'/test.txt'
    lines = [x.strip() for x in open(infile)]

    points = []
    for r in range(0,1000):
        points.append(["." for c in range(0,1000)])

    grid = Grid(points)


    pass