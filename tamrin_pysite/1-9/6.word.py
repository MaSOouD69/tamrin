while 1:
    print("\033c", end="")
    word= input("Enter the word to analyze: ")
    wordb=word[::-1]
    if word==wordb:
        print (f"   {word} is backward")
        input("Enter to continue")
    else:
        print(f"   {word} is Not backward")
        input("Enter to continue")
