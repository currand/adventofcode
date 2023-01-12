import re

test1 = 'aabcdefgaa'
test2 = 'aaa'
test3 = 'xazegov'
test4 = 'aabbccdd'

naughty = [
    'jchzalrnumimnmhp',
    'haegwjzuvuyypxyu',
    'dvszwmarrgswjxmb'
]

nice = [
    'ugknbfddgicrmopn',
    'aaa',
]

bad_strings = [
    'ab',
    'cd',
    'pq',
    'xy'
]
vowels = '[aeiouAEIOU]'

def vowel_func(string):
    pattern = re.compile(vowels)
    result = pattern.findall(string)
    if len(result) < 3:
        return False
    else:
        return True
        
def twice_func(string):
    pattern = re.compile(r'(..)\1{1}')
    result = pattern.findall(string)
    if len(result) > 0:
        pattern = re.compile(r'(.')
    else:
        return False

def has_strings(string):
    for line in bad_strings:
        if line in string:
            return True
    return False

def check_string(string):
    if vowel_func(string) is True and \
        twice_func(string) is True and \
        has_strings(string) is False:
        return True
    else:
        return False


assert vowel_func(test1) is True
assert vowel_func(test2) is False
# assert twice_func(test1) is False
# assert twice_func(test4) is True
# assert has_strings(test4) is True
# assert has_strings(test3) is False
for string in naughty:
    assert check_string(string) is False
for string in nice:
    assert check_string(string) is True

if __name__ == "__main__":
    naughty = 0
    nice = 0
    with open('prob5.in') as fh:
        strings = fh.readlines()
    for string in strings:
        if check_string(string) is True:
            nice += 1
        else:
            naughty += 1

    print(nice)