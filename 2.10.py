f = open('input.txt').read()
new = ''
for letter in range(len(f)):
    if f[letter] in 'уеыаоэяиюё':
        if f[letter - 1] not in 'уеыаоэяиюё':
            new += 'c' + f[letter]
        else:
            if f[letter + 1] not in 'уеыаоэяиюё':
                new += 'c' + f[letter]
            else:
                new += f[letter]
    else:
        new += f[letter]
print(new)
