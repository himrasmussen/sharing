'''
SimpleKey
chra94
'''

import random
key = ''
letters = 'abcde'
def generate():
    global key
    for i in range(5):
        key += str(random.randint(0, 9))
        key += letters[random.randint(0, 4)]
        
    print(key)

def validate():
    key = input('Enter key')
    n = len(key)
    for i in key:
        print(i)
        print(n)
        #On even places in key
        if n % 2 == 0:
            int(i)
        else:
            str(i)

        n -= 1
        
    print('Success')       
        
        
decide = input('Generate/Validate?')
if decide == 'Generate':
    generate()
elif decide == 'Validate':
    validate()
