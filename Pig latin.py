'''
Pig Latin
chra94 -|-
'''


word = input('enter a word') 
word += '-' + word[0] + 'ay'
word = word[1:]
print (word)
