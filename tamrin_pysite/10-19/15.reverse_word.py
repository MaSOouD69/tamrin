def rev_word(word):
    l=word.split(" ")
    newll=l[::-1]
    st=" ".join(newll)
    return st
while 1:
    print('\033c', end="")
    print(rev_word(input("Type in Your sentence for reverse: ")))
    input("ENTER")
