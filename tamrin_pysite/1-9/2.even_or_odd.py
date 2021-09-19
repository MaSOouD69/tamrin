while 1:
    print("\033c", end='')
    num= input("Enter the number:")
    if int(num)%4==0 and int(num)>0: print(" 4 is the numbers divider ")
    elif int(num)%2==0 and int(num)>0: print("the number is even")
    elif int(num)%2==1 and int(num)>0: print ("the number is odd")
    else: print("bad input \ntry again")
    input(" press ENTER to continue")