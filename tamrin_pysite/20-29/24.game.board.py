print("\033c", end="")
size = int(input("size of the game board you wish?? "))
print("\033c", end="")
for i in range(size):
    print(size * ' ---')
    print((size+1)*'|   ')
print(size * ' ---')