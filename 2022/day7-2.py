from __future__ import annotations
import re
from utils.utils import get_input
from dataclasses import dataclass


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

def calc_sizes(node: Node) -> None:
    """ 
    Recurse backwards through the nodes. For each child add a recursion step
    once you've reached the bottom, do the stuff. To recurse top to bottom, do the stuff,
    THEN do the recursion.

    This function adds the file sizes to their directory size and then sets the parent.
    Finally, add the '/' directory size to the total.

    """
    for child in node.children.values():
        calc_sizes(child)
    if node.parent is not None:
            node.parent.total_size += node.size + node.total_size
    else:
            node.total_size += node.size

    print(f'{node.name}: {node.size}, {node.total_size}')

def print_size_p1(node):
    global sizes_p1
    for child in node.children.values():
        print_size_p1(child)
    if node.size + node.total_size <= 100000:
        sizes_p1.append(node.size + node.total_size)

def print_size_p2(node):
    # The part 2 solution only counts directories above 40000000 minus the size of '/'
    global sizes_p2
    for child in node.children.values():
        print_size_p2(child)
    if node.size + node.total_size >= fs.root.total_size - 40000000:
        sizes_p2.append(node.size + node.total_size)

if __name__ == '__main__':

    lines = get_input('day7.txt')
    fs = Filesystem()

    sizes_p1 = []
    sizes_p2 = []

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

    calc_sizes(fs.root)
    print_size_p1(fs.root)
    print_size_p2(fs.root)
    print('p1:', sum(sizes_p1))
    print('p2:', min(sizes_p2))
