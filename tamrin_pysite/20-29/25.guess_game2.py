print("\033c",end="")
print("****HELLO WELLCOME TO GUESS NUMBER GAME****")
print("Pick a random number between 1 & 100: \n")
input("  * Enter to continue *  ")
a=0
b=101
count=0
y=''
while y!="exit":
    x=(a+b)//2
    y=input(f"{x}, is Your number??(yes/too high/too low): ").lower()
    count +=1
    if y=="yes":
        print("THANK YOU", count,"TRIES")
        input("  * Enter to continue *  ")
        break
    elif y=="too high":
        b=x
        continue
    elif y=="too low":
        a=x
        continue
