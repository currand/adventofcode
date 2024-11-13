import os

TEST = False

filedir = os.path.dirname(__file__)
day = filedir[-2:]
if TEST:
    infile = filedir + f'/test{day}.txt'
else:
    infile = filedir + f'/day{day}.txt'

lines = [x.strip() for x in open(infile, 'r')]

if __name__ == '__main__':
    pass
