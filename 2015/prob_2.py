
with open("prob_2.in") as fh:
    prob_input = fh.readlines()

def calc_area(l, w, h):
    side1 = l*w
    side2 = w*h
    side3 = l*h
    return min(side1, side2, side3), 2*side1 + 2*side2 + 2*side3

def calc_bow(l, w, h):
    bow = l*w*h
    sides = sorted([l, w, h])
    length = 2*sides[0] + 2*sides[1]

    return length + bow


total_sq_ft = 0
total_bow_ft = 0

for line in prob_input:
    l, w, h = [int(x) for x in line.split('x')]

    min_side, current_sq_ft = calc_area(l, w, h)
    current_sq_ft += min_side

    total_sq_ft += current_sq_ft

    bow_ft = calc_bow(l,w,h)
    total_bow_ft += bow_ft

print(total_sq_ft)
print(total_bow_ft)