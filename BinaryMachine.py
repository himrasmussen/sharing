'''
Binary Machine 10
Chra94
'''


def binary():
    binary = input('Enter a binary number')
    n = -1
    s = 0
    for i in binary[::-1]:
        n += 1
        if i == '1':
            s += 2**n
    print(s)


def base10():
    binary = int(input('Enter Binary'), 2)
    print(binary)


while True:
    mode = input('Enter binary or base 10 number?')
    if mode == 'binary':
        binary()
    elif mode == 'base 10':
        base10()
    else:
        print('Try again')
