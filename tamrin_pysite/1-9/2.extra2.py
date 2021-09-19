while 1:
    print("\033c",end="")
    num= input("Enter the number:")
    chek= int(input("Enter the cheker:"))
    if int(num)%chek==0 and int(num)>0: print("the cheker is number's divider")
    else: print("the cheker is NOT number's divider")
    input(" press ENTER to continue")