with open("day1.in", 'r') as fh:
    lines = fh.readlines()

result = 0

found = False
frequencies = []

while found is False:
    for line in lines:
        op = line[0]
        x = int(line[1:-1])

        if op == "+":
            result = result + x
        elif op == "-":
            result = result - x
        
        if result not in frequencies:
            frequencies.append(result)
        else:
            found = True
            break

print(result)