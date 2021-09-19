import random

def compar_cow(num,guess):
    cow=0
    for i in range(len(num)):
        if num[i]==guess[i]: cow+=1
    return cow

def compar_bull(num,guess):
    bull=0
    for i in range(len(num)):
        for j in range(len(guess)):
            if i!=j and num[i]==guess[j]: bull+=1
    return bull

while 1:
    print("\033c", end="")
    num=str(random.randint(1000,9999))
    count=0
    while 1:
        print("\033c",end="")
        guess=input("Whats lucky number: ")
        cow=compar_cow(num,guess)
        bull=compar_bull(num,guess)
        count+=1
        if cow==4:
            print("Exact ",count, " tries")
            break
        elif cow+bull==4:
            print(f"Nice, {cow} Cow and {bull} Bull, ",count, " tries")
        else: print(f"Try Again, {cow} Cow and {bull} Bull, ",count," tries")
#        print(num, cow, bull, count, "tries")
        input("enter")