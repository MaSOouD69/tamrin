#barnameye hadse addad 4 raghami
import random
#tabdil addad 4 raghami b 4 addad
def splite(num):
    x1=num//1000
    x2=(num- x1*1000)//100
    x3=(num-x1*1000 - x2*100)//10
    x4=(num-x1*1000 - x2*100 -x3*10)
    return x1,x2,x3,x4
# tedad argham dorost 2 adad
def approx(num1, num2):
    match=0
    for itemx in splite(num1):
        for itemy in splite(num2):
            if itemx==itemy:
                match+=1
                break
    return match

def list_approx(num1, num2):
    lis=[]
    for item1 in splite(num1):
        for item2 in splite(num2):
            if item1==item2:lis.append(item1)
    return lis

def min_approx(num1,num2):
    match1=approx(num1,num2)
    match2=approx(num2,num1)
    return min(match1,match2)

# match kardan addad 2 addad ba ham
def match(num1,num2):
    lis=[]
    num1=list(splite(num1))
    num2=list(splite(num2))
    for i in range(4):
        if num1[i]==num2[i]:
            lis.append(num1[i])
    return lis
#sakht addad 4 raghami random
def num_random():
    item=0
    num=[]
    use=""
    while len(num)<4:
        item=str(random.randint(0,9))
        if item not in num:
            num.append(item)
    for elem in num:
        use += elem
    return use

def wellcome():
    print("***WELLCOME TO GUESS NUMBER***")
    print("YOU SHOULD GUESS A 4 DIGIT NUMBER")
#choose difficulty
def set_difficulty():
    diffic=input("Choose the difficulty(easy/hard):").lower()
    if diffic=="easy": return 5
    elif diffic=='hard': return 3

while True:
    wellcome()
    input("ENTER TO CONTINUE")
    print("\033c",end="")
    diffic=set_difficulty()
#    print(diffic)
    num=int(num_random())
    count=1
    while diffic <= count:
        if count >= diffic:
            print(f"Your turn is over, num is {num}")
        else:
            num1=int(input("Enter your Guess: "))
            i=match(num1,num)
            j=list_approx(num1,num)
            if len(i)<4:
                print(f" {j} is in the number, only {i} is in right place,")
                count+=1
            else:
                print("***YOUR GUESS IS CORRECT***")
                x=input("choose the option(EXIT/CONTINUE)? ").lower()
                if x==("exit"): break
                else: continue
    x=input("continue?? (y/n): ").lower()
    if x=="n": break
print("***GOOD BYE***")
    