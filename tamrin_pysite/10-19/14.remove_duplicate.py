def remove_dup(list1):
    new_list=[]
    for item in list1:
        if item not in new_list:
            new_list.append(item)
    return new_list

x=[1,2,3,4,6,7,8,9,3,2,4,5,6,7,8,9,0,3,2,1,22,44,55,6,778]
print(remove_dup(x))