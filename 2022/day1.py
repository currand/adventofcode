def get_input(filename):
    with open(filename, 'r') as fh:
        lines = fh.readlines()
        return [line.strip() for line in lines]



if __name__ == '__main__':
    lines = get_input('day1.txt')

    out = []
    x = 0
    for i in lines:
        if i != '':
            x = x + int(i)
        else:
            out.append(x)
            x = 0
        
        
    
    s = sorted(out, reverse=True)
    top = s[0]
    top3 = sum(s[0:3])
    pass
