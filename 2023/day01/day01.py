import os

filedir = os.path.dirname(__file__)
day = filedir[-2:]
infile = filedir + f'/day{day}.txt'
testfile = filedir + f'/test{day}.txt'
lines = [x.strip() for x in open(infile)]


if __name__ == '__main__':
    out = []
    nums = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    for line in lines:
        digits = []
        break_outer = False
        word = []

        for x in line:
            
            word.append(x)
            for key in nums.keys():
                if key in ''.join(word):
                    digits.append(nums[key])
                    break_outer = True
                    break
                elif x.isdigit():
                    digits.append(x)
                    break_outer = True
                    break
            if break_outer:
                 break
        
        word = []
        break_outer = False
        for x in line[::-1]:
            
            word.append(x)
            for key in nums.keys():
                if key[::-1] in ''.join(word):
                    digits.append(nums[key])
                    break_outer = True
                    break
                elif x.isdigit():
                    digits.append(x)
                    break_outer = True
                    break
            if break_outer:
                 break
        
        out.append(int(''.join(digits)))
    print(sum(out))
            




