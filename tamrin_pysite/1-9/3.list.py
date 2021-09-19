empty=list()
a=[1,2,3,4,5,6,7,8,9,98,76,54,32,12,45]
b=[i for i in a if i<10]
for item in a:
    if item<10:
        empty.append(item)
print(empty)
print(b)