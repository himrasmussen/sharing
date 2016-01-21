string = 'Ja vi elsker dette landet som det stiger frem.'
reverse = ''

n = len(string) - 1

for i in string:
    reverse += string[n]
    n -= 1

print(reverse)
