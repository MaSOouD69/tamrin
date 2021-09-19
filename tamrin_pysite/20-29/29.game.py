import re
# x = 1
# o = 2
# empty = 0

def input_game(r , c, person):
    if person =="M": game[r][c] = "M"
    elif person == "N": game[r][c] = "N"
    return game
def print_game():
    for i in range(3):
        print(3 * ' ---')
        print('| {} | {} | {} |'.format(game[i][0],game[i][1],game[i][2]))
    print(3 * ' ---')

def checkGrid(grid):
	# rows
	for x in range(0,3):
		row = set([grid[x][0],grid[x][1],grid[x][2]])
		if len(row) == 1 and grid[x][0] != '0':
			return grid[x][0]

	# columns
	for x in range(0,3):
		column = set([grid[0][x],grid[1][x],grid[2][x]])
		if len(column) == 1 and grid[0][x] != '0':
			return grid[0][x]

	# diagonals
	diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
	diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
	if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != '0':
		return grid[1][1]

	return 0

game = [['0','0','0'],
        ['0','0','0'],
        ['0','0','0']]

count = 0 # number of places which is filed

while count<9:
    print("\033c", end='')
    print_game()
    if count%2 == 0:person = "N"
    else: person = "M"
    x = input(f"Enter the row and column ,player {person}, (seperate by ','): ")
    try:
        if re.search("^[1-3],[1,3]$", x):
            r = int(x.split(",")[0].strip()) - 1
            c = int(x.split(",")[1].strip()) - 1
        
    except:
        print("Your digit is Not according to Ex (1,2): ")
        input("**#Enter to continue#**")
        continue
    if game[r][c]=='0':input_game( r , c , person)
    else:
        print(f"player {person}, your choise is filled allright")
        print("please choose another place")
        input("Enter to continue")
        continue
    count += 1
    g = checkGrid(game)
    print(g)
    input("Enter to continue")
print("\033c", end='')
print("***Game End***")
print_game()