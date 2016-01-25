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
    binary = 0
    base10 = input('Enter')
    while int(base10) > 1:
        int(base) - 1 
