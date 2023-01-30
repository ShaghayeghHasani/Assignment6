import pyfiglet
def game():
    for row in game_board:
        for cell in row:
            print(cell," " ,end= "")
        print()
title = pyfiglet.figlet_format("Tic Tac Toe" , font = "slant")
print(title)

def check_game ():

    if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X" :
        print ("Player one wins!")
            
    if game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O" :
        print ("Player two wins!")
    
    if game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X" :
        print("Player one wins!")
    
    if game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O" :
        print("Player two wins!")
    
    if game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X" :
        print("Player one wins!")
    
    if game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O" :
        print("Player two wins!")
    
    if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X" :
        print("Player one wins!")
    
    if game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O" :
        print("Player two wins!")
    
    if game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X" :
        print("Player one wins!")
    
    if game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O" :
        print("Player two wins!")
    
    if game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X" :
        print("Player one wins!")
    
    if game_board[0][2] == "O" and game_board[1][2] == "O" and game_board[2][2] == "O" :
        print("Player two wins!")
    
    if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X" :
        print("Player one wins!")
    
    if game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O" :
        print("Player two wins!")
    
    if game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X" :
        print("Player one wins!")
    
    if game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O" :
        print("Player two wins!")   
    
    if game_board[0][0] != "-" and game_board[0][1] != "-" and game_board[0][2] != "-" and game_board[1][0] != "-" and game_board[1][1] != "-" and game_board[1][2] != "-" and game_board[2][0] != "-" and game_board[2][1] != "-" and game_board[2][2] != "-" :
        print("It's a draw!")    

game_board = [[ "-" , "-" , "-" ],
              [ "-" , "-" , "-" ],
              [ "-" , "-" , "-" ]]
game()

while True:
    # player one
    print("PLayer one GO!")
    while True:
        row = int(input("row= "))
        column = int(input("column= "))
        if 0 <= row <=2 and  0 <= column <=2 :
            if game_board[row][column] == "-":
                game_board[row][column] = "X"
                game()
                check_game()
                break
            else:
                print("Choose another cell!")
        else:
            print ("Choose between 0 and 2")
    #player two
    print("Player two GO!")
    while True:
        row = int(input("row= "))
        column = int(input("column= "))
        if 0 <= row <=2 and  0 <= column <=2 :
            if game_board[row][column] == "-":
                game_board[row][column] = "O"
                game()
                check_game() 
                break
            else:
                print("Chose another cell!")
        else:
            print ("Chose between 0 and 2")
   
        game()