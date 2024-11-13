import os
from typing import Union
from collections import Counter, OrderedDict

TEST = True

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

# def calc_winners(queue: list, cards: dict, max_card: int, card_count: int = 0) -> Union[list, bool]:
#     ''' 
#     Recursive

#     base case - there are no cards left (max_card)

#     1. Get the number of wins for the current card
#     2. for each of those cards, repeat step one

#     '''
#     if len(queue) == 0:
#         return card_count
#     else:
#         card = queue.pop(0)
#         num_winners = len(cards[card]['intersect'])
#         card_count += num_winners
#         new_cards = [n for n in range(card+1, card + num_winners+1) if n <= max_card]
#         queue += new_cards
#         queue = sorted(queue)
#         return calc_winners(queue, cards, max_card, card_count)
        
    
def calc_winners(cards):
    winners = []
    for k in cards.keys():
        winners *= [x for x in range(k + 1, k + len(cards[k]['intersect']) + 1) if x <= max(cards.keys())]
        pass

cards = {x['name']: x for x in [parse_card(line) for line in lines]}

card_count = calc_winners(cards)

print(f"{card_count=}")

