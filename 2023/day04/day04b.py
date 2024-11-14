import os
from typing import Union
from collections import Counter, OrderedDict

TEST = False

filedir = os.path.dirname(__file__)
day = filedir[-2:]
if TEST:
    infile = filedir + f'/test{day}.txt'
else:
    infile = filedir + f'/day{day}.txt'

with open(infile, 'r') as f:
    lines = [line.strip() for line in f]

def parse_card(card: str) -> dict:
    output = {}
    name, numbers = card.split(':')
    winners, nums_have = numbers.split(' | ')
    output['name'] = int(name.replace('Card ', ''))
    output['winners'] = {int(x) for x in winners.split()}
    output['nums_have'] = {int(x) for x in nums_have.split()}
    output['intersect'] = output['winners'].intersection(output['nums_have'])

    return output
        
    
def calc_winners(cards):
    cards_won = list(cards.keys())
    queue: list[int] = [x for x in cards.keys()]
    while queue:
        winners = []
        card = queue.pop(0)
        winners = [x for x in range(card + 1, card + len(cards[card]['intersect']) + 1) if x <= max(cards.keys())]
        queue += winners
        cards_won += winners
    return len(cards_won)

cards = {x['name']: x for x in [parse_card(line) for line in lines]}

card_count = calc_winners(cards)

print(f"{card_count=}")