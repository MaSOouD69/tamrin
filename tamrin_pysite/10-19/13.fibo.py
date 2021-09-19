def fibo(num):
    if num==1: return 1
    elif num==2: return 1
    else:
        count=0
        while count<=num:
            count+=1
            fibon=fibo(num-1)+fibo(num-2)
        return fibon
while 1:
    print("\033c")
    print(fibo(int(input("whats the number ?? its fibo time!!!: "))))
    input("Enter to continue")