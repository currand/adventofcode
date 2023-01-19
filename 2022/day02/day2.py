from enum import Enum
import os

filedir = os.path.dirname(__file__)
day = filedir[-2:]
infile = filedir + f'/day{day}.txt'
testfile = filedir + f'/test{day}.txt'
lines = [x.strip() for x in open(infile)]
games = [tuple(x.split(' ')) for x in lines]

winners = {
    ("A", "X"): "draw",
    ("A", "Y"): "win",
    ("A", "Z"): "lose",
    ("B", "X"): "lose",
    ("B", "Y"): "draw",
    ("B", "Z"): "win",
    ("C", "X"): "win",
    ("C", "Y"): "lose",
    ("C", "Z"): "draw",
}

class Scores(Enum):
    ROCK = 1 # A, X
    PAPER = 2 # B, Y
    SCISSORS = 3 # C, Z
    A = 1
    B = 2
    C = 3
    X = 1
    Y = 2
    Z = 3
    LOST = 0
    DRAW = 3
    WON = 6

total = 0
for game in games:
    score = 0
    if winners[game] == 'win':
        score = Scores.WON.value + Scores[game[1]].value
    elif winners[game] == 'lose':
        score = Scores.LOST.value + Scores[game[1]].value
    elif winners[game] == 'draw':
        score = Scores.DRAW.value + Scores[game[1]].value
    else:
        print("Not found")
    
    total += score
    
print(total)