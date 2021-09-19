while True:
    print("\033c", end="")
    try:
        num = abs(int(input("Please Enter Number: ")))
        divid=num//2 + 1
        dividers=[i for i in range(2,divid) if num%i==0]
        print(f'the dividers of {num} is :', dividers)
        input("please Enter To continue")
    except ValueError:
        print("Bad input!!!  Not a number")
        input("please Enter To continue")
