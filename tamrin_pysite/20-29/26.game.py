def winner(game):
    # rows
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] and game[i][0] != 0 :
            if game[i][0] == 1:return "1"
            else:return "2"
    
    # columns
    for i in range(3):
        if game[0][i] == game[1][i] == game[2][i] and game[0][i] != 0 :
            if game[0][i] == 1:return "1"
            else:return "2"

        
    # diagonals
    for i in range(3):
        if game[0][0] == game[1][1] == game[2][2] and game[i][i] != 0 :
            if game[i][i] == 1:return "1"
            else:return "2"

x =[[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]
m = winner(x)
if m == None:
    print("No winner")
elif m == "1":
    print(" player 1 win")
elif m == '2':
    print(" player 2 win")