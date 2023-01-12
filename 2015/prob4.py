import hashlib

test1 = 'abcdef'
answer1 = 'abcdef609043'
test2 = 'pqrstuv'

problem = 'iwrupvqb'

a = 0

while True:
    new_string = problem + str(a)
    result = hashlib.md5(new_string.encode())
    first_5_char = result.hexdigest()[:6]
    print(a, result.hexdigest()[:6])
    if first_5_char == '000000':
        print("Success!: {}".format(a))
        break
    a += 1