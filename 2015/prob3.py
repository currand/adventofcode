
with open("prob3.in") as fh:
    dirs = fh.readline()

santa_locs = {
    (0, 0): 1
}
robo_locs = {
    (0, 0): 1
}

santa_current_pos = [0, 0]
robo_current_pos = [0, 0]

who = 0

for i in dirs:

    if who == 0:
        current_pos = santa_current_pos
    else:
        current_pos = robo_current_pos

    if i == '^':
        current_pos[1] += 1
    elif i == 'v':
        current_pos[1] -= 1
    elif i == '<':
        current_pos[0] -= 1
    else:
        current_pos[0] += 1

    key = tuple(current_pos)

    if who == 0:
        who = 1
        if key in santa_locs.keys():
            santa_locs[key] += 1
        else:
            santa_locs[key] = 1
    else:
        who = 0
        if key in robo_locs.keys():
            robo_locs[key] += 1
        else:
            robo_locs[key] = 1

houses = [tuple(x) for x in robo_locs.keys()]
houses += [tuple(x) for x in santa_locs.keys()]

print(len(set(houses)))
