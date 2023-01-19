import os

filedir = os.path.dirname(__file__)
day = filedir[-2:]
infile = filedir + f'/day{day}.txt'
testfile = filedir + f'/test{day}.txt'
lines = [x.strip() for x in open(infile)]



if __name__ == '__main__':
    

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
    print(top)
    print(top3)
