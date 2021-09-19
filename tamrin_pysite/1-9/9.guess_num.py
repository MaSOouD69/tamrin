import random

guess=1
while guess!=0:
    count=0
    print("\033c",end='')
    while 1:
        difficulty= input("please choose the difficulty (easy / hard) : ").lower()
        if difficulty=="easy":
            point=5
            break
        elif difficulty=="hard":
            point=3
            break
        else:
            print("your input not valid")
    num=random.randint(1,9)
    print("\033c",end='')
    while guess!=0:
        if count>=point:
            print("your turn is over")
            print( "\n" + f"the number is {num}"+"\n")
            break
        elif count<point:
            guess=int(input("guess the number between 1 and 9? (0 to EXIT): "))
            count += 1
            if guess==0:
                break
            elif guess<1 or guess>9 :
                print ("not valid Guess"+"\n")
                count-=1
                continue
            elif num<guess:
                print("too high"+"\n")
            elif num>guess:
                print("too low"+"\n")
            elif num==guess:
                print(f"'EXACT': the number is {num}"+"\n")
                input("Enter to continue")
                print("\033c",end='')
                break
            elif count==point:
                print("your turn is over")
                input("press Enter to continue")
                break
    input("press Enter to continue")