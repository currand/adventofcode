from __future__ import annotations
import re
from utils.utils import get_input

class Node():

    def __init__(self, name: str, parent: Node | None, size: int | None = None) -> None:
        self.name = name
        self.parent = parent
        self.children = {}
        self.files = {}
        self.size = 0
        self.total_size = 0
    
    def add_file(self, name, size) -> None:
        self.files[name] = int(size)
        self._update_size()
    
    def _update_size(self) -> None:
        self.size = sum([n for n in self.files.values()])
        self.total_size = self._calc_size(self.size)

    def _calc_size(self, size):
        for node in self.children.values():
            if node == None:
                return
            self.total_size = self.size
            return self._calc_size(node, total_size)

class Filesystem():

    def __init__(self) -> None:
        self.root: Node = Node('/', None)
        self.curr_dir: Node = self.root
    
    def __repr__(self) -> None:
        print(self.curr_dir[name])

    def add_dir(self, name) -> None:
        self.curr_dir.children[name] = Node(name=name, parent=self.curr_dir)

    def add_file(self, name, size) -> None:
        self.curr_dir.add_file(name, size)

    def cd_up(self) -> None:
        self.curr_dir = self.curr_dir.parent
    
    def cd(self, name) -> None:
        self.curr_dir = self.curr_dir.children[name]

if __name__ == '__main__':

    lines = get_input('test7.txt')
    fs = Filesystem()

    cd = re.compile(r'\$\s+cd\s+(.*)')
    dir = re.compile(r'dir\s+(.*)')
    file = re.compile(r'(\d+)\s+(.*)')

    for line in lines:
        
        if matches:= cd.match(line):
            name = matches.group(1)
            if name == '/':
                fs.curr_dir = fs.root
            elif name == '..':
                fs.cd_up()
            elif name in fs.curr_dir.children:
                fs.cd(name)
            else:
                fs.add_dir(name)
                fs.cd(name)
        elif matches:= dir.match(line):
            name = matches.group(1)
            if name not in fs.curr_dir.children:
                fs.add_dir(name)
        elif matches:= file.match(line):
            name = matches.group(2)
            size = matches.group(1)
            if name not in fs.curr_dir.children:
                fs.add_file(name, size)
        else:
            pass



pass
