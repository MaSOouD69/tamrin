b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x=list()
for item in a:
    for elem in b:
        if item not in x and item == elem:
            x.append(item)
            break
print(x)