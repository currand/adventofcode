import os

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

max_card = len(lines)
cards_to_process = list()
cards_seen = dict()

for line in lines:
    card = parse_card(line)
    won = len(card['intersect'])
    if card['name'] not in cards_seen.keys():
        cards_seen[card['name']] = 1
    else:
        cards_seen[card['name']] += 1
    cards_to_process += range(card['name'] + 1, won + 2)

pass