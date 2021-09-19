#prime number
def divider(num):
    divids=[]
    divid=num//2+1
    for i in range(2,divid):
        if num%i==0:
            divids.append(i)
    return divids
while 1:
    print("\033c", end='')
    num=int(input("Enter the number: "))
    if divider(num)==[]:
        print(f"{num} is PRIME")
        input("Enter to continue")
    else:
        s=str(divider(num))
        print(f"{num} is NOT prime, it's divider's are: \n {s}")
        input("Enter to continue")