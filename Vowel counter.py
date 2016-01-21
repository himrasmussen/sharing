vowel = 'aeiouy'
words = 'One two three four five six seven eight nine thousand'
n = 0
dictionary = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'y': 0}
for i in words:
    if i in vowel:
        n += 1
        if i == vowel[0]:
            dictionary['a'] += 1
        elif i == vowel[1]:
            dictionary['e'] += 1
        elif i == vowel[2]:
            dictionary['i'] += 1
        elif i == vowel[3]:
            dictionary['o'] += 1
        elif i == vowel[4]:
            dictionary['u'] += 1
        elif i == vowel[5]:
            dictionary['y'] += 1

print(n)
for i in dictionary.items():
    print(i)
