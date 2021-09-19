def get_first_last(j):
    first=j[0]
    last=j[len(j)-1]
    return first,last

x=list()
for item in range(10):
    l=input(f"enter the num {item+1}'st : ")
    x.append(l)

first,last=get_first_last(x)
print(f'the first entered is {first} and last enterd is {last}')
