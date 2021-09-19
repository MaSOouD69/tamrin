def re_dup(list1):
    new=set()
    for item in list1:
        new.add(item)
    return new


x=[1,2,3,4,6,7,8,9,3,2,4,5,6,7,8,9,0,3,2,1,22,44,55,6,778]
print(re_dup(x))