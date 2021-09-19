# x = 1
# o = 2
# empty = 0

def input_game(r , c, person):
    if person =="x": game[r][c] = "1"
    elif person == "o": game[r][c] = "2"
    return game

game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

count = 0 # number of places which is filed

while count<9:
    if count%2 == 0:person = "x"
    else: person = "o"

    x = input(f"Enter the row and column ,player {person}, (seperate by ','): ")
    r = int(x.split(",")[0].strip()) - 1
    c = int(x.split(",")[1].strip()) - 1
    if game[r][c]==0:input_game( r , c , person)
    else:
        print(f"player {person}, your choise is filled allright")
        print("please choose another place")
        continue
    count += 1

print(game)