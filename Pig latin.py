'''
Pig Latin
chra94 -|-
'''

while True:
    word = input('enter a word (blank to quit)\n')
    if word == '':
        break
    word += '-' + word[0] + 'ay'
    word = word[1:]
    print (word)
