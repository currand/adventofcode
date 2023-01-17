from enum import Enum
from utils.utils import get_input
from anytree import Node, RenderTree

lines = get_input('day2.txt')
games = [tuple(x.split(' ')) for x in lines]


class Scores(Enum):
    ROCK = 1 # A, X
    PAPER = 2 # B, Y
    SCISSORS = 3 # C, Z
    A = 1
    B = 2
    C = 3
    X = 0
    Y = 3
    Z = 6

winners = {
    ("A", "X"): Scores.SCISSORS,
    ("A", "Y"): Scores.ROCK,
    ("A", "Z"): Scores.PAPER,
    ("B", "X"): Scores.ROCK,
    ("B", "Y"): Scores.PAPER,
    ("B", "Z"): Scores.SCISSORS,
    ("C", "X"): Scores.PAPER,
    ("C", "Y"): Scores.SCISSORS,
    ("C", "Z"): Scores.ROCK,
}

total = 0
for game in games:
    score = winners[game].value + Scores[game[1]].value    
    total += score
    
print(total)