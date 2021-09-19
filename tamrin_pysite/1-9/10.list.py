a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
m=[i for i in a if i in b]
n=[]
for i in m:
    if i not in n:
        n.insert(-len(n),i)
print(n)