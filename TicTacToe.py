board = ["-", "-" , "-",
         "-", "-" , "-",
         "-", "-" , "-"]

isGameOn = True

winner = None

curPlayer = "X"

def game_start():

    #Printing the Board
    displayBoard()

    #Verifying if game is still going to switch players
    while isGameOn :
        playing_turn(curPlayer)

        isGameOver()

        switchPlayer()
    
    if winner  == "X" or winner == "O":
        print(winner  + " won.")
    elif winner == None:
        print("Tie.")

def displayBoard():
      print("\n")
      print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
      print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
      print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
      print("\n")

    


def isGameOver():
    playerWin()

    playersTie()





#Checking if one player Won
def playerWin():
    global winner

    rowWin = rowVerify()
    columnsWin = columnsVerify()
    diagWin = diagVerify()

    if rowWin:
        winner = rowWin
    elif columnsWin:
        winner = columnsWin
    elif diagWin:
        winner = diagWin
    else:
        winner = None


#Checking if the Players did a tie
def playersTie():
    global isGameOn 

    #Board is Full but no player Won
    if "-" not in board:
        isGameOn = False
        return True

    else:
        return False



def columnsVerify():
    global isGameOn

    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3:
        isGameOn = False

    if column1:
        return board[0] 
    elif column2:
        return board[1] 
    elif column3:
        return board[2] 
    #Tie
    else:
        return None

    

def rowVerify():
    global isGameOn

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        isGameOn = False

    if row1:
        return board[0] 
    elif row2:
        return board[3] 
    elif row3:
        return board[6] 
    #Tie
    else:
        return None

def diagVerify():
    global isGameOn


    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"

    if diag1 or diag2:
        isGameOn = False

    if diag1:
        return board[0]
    elif diag2:
        return board[2]
    else:
        return None




def switchPlayer():
    global curPlayer

    if curPlayer == "X":
        curPlayer = "O"
    elif curPlayer == "O":
        curPlayer = "X"
    



#handling turns
def playing_turn(player):
    #Get the player to choose a position
    print(player+"'s Turn :")
    position = input("choose a place between 1 and 9 : ")

    #handling position errors
    validMove = False
    while not validMove:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            validMove = True
        else:
            print("Wrong move try Again")


    board[position] = player

    displayBoard()


#Game Starting
game_start()