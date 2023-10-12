def split(n, r):
    temp = 0
    list = []
    length = len(r)
    for i in range(len(n)):
        if n[i:i + length] == r:
            list.append(n[temp:i], )
            temp = i + length

    list.append(n[temp:len(n)])
    print(list)


split('Geeks 123 For 123 Geeks', ' ')
print('Geeks123For123Geeks'.split())

print(' '.join('Geeks123For123Geeks'.split('123')))