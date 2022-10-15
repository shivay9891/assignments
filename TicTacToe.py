#TIC TAC TOE GAME : Bole to : X-O Game

#Task to be completed
#1. Declare array of 9 with '__'
#2. make nice format to print it
#3. Write winning condition
#4. specify turns
#5. Take input in the specific position
#6. see if someone won and declare winner
#7. see if more turns left yes or no
#8. Repeat the game if turns are over

# isEmpty? function
def isEmpty(xoList):
    count =0 
    for i in range(9):
        if xoList[i] ==' ':
            count+=1
    if count !=0:
        return 1 #empty points available
    else:
        print('It is a Draw')
        return 2 #empty points not available

# Creating XO list 
def emptyList_XO():
    tmp_list = []
    for i in range(9):
        tmp_list.append(' ')
    return tmp_list

# printBoard function
def printBoard(xo):
    print(xo[0], "|",xo[1], "|",xo[2])
    print('----------')
    print(xo[3], "|",xo[4], "|",xo[5])
    print('----------')
    print(xo[6], "|",xo[7], "|",xo[8])

# Selecting the first player to play randomely
import random
def whoWillGoFirst():
    player= random.randint(0,1)
    if player==0:
        print("Player A will go first with O")
    else:
        print("Player B will go first with X")
    return player

# taking input
def takeInput(player, xoList):
    print("Hay Player, ", player)
    flag=0
    while flag==0:
        pos = int(input('Enter the position in between [ 0 to 8 ] - '))
        if pos>= 0 and pos<=8:
            if xoList[pos]==' ':
                print('Valid Input')
                if player==0:
                    xoList[pos] = 'X'
                else:
                    xoList[pos] = 'O'
                return xoList
                flag=1
            else:
                print('Please Enter Again, It\'s occupied')
                flag = 0
        else:
            print('Please Give Valid Input Again')
            flag = 0

# function for checking winner
def checkWin(xoList):    #012 456 678 036 147 258 048 246 pairs to win the game
    if xoList[0] == 'X' and xoList[1] == 'X' and xoList[2] == 'X' or xoList[3] == 'X' and xoList[4] == 'X' and xoList[5] == 'X' or xoList[6] == 'X' and xoList[7] == 'X' and xoList[8] == 'X' or xoList[0] == 'X' and xoList[3] == 'X' and xoList[6] == 'X' or xoList[1] == 'X' and xoList[4] == 'X' and xoList[7] == 'X' or xoList[2] == 'X' and xoList[5] == 'X' and xoList[8] == 'X' or xoList[0] == 'X' and xoList[4] == 'X' and xoList[8] == 'X' or xoList[2] == 'X' and xoList[4] == 'X' and xoList[6] == 'X':
        print('Player A is Winner')
        return 2
    elif xoList[0] == 'O' and xoList[1] == 'O' and xoList[2] == 'O' or xoList[3] == 'O' and xoList[4] == 'O' and xoList[5] == 'O' or xoList[6] == 'O' and xoList[7] == 'O' and xoList[8] == 'O' or xoList[0] == 'O' and xoList[3] == 'O' and xoList[6] == 'O' or xoList[1] == 'O' and xoList[4] == 'O' and xoList[7] == 'O' or xoList[2] == 'O' and xoList[5] == 'O' and xoList[8] == 'O' or xoList[0] == 'O' and xoList[4] == 'O' and xoList[8] == 'O' or xoList[2] == 'O' and xoList[4] == 'O' and xoList[6] == 'O':
        print("Player B is Winner")
        return 2
    else:
        # Checking for avaibility of spaces to write
        if isEmpty(XO_list)==1:
            return 1
        else:
            return 2
        #count =0
        #for i in range(9):
        #    if xoList[i] == ' ':
        #        count = count+1
        #if count !=0:
        #    return 1 #empty points available
        #else:
        #    print('It is a Draw')
        #    return 2 #empty points not available

# All functions are completed
# The Game Begins

XO_list = emptyList_XO()
printBoard(XO_list)
scoreA =0 
scoreB =0
gameStatus = 0
play = whoWillGoFirst()

while gameStatus != 2 :

    if play == 0:
        XO_list = takeInput(0, XO_list)
        printBoard(XO_list)
        gameStatus = checkWin(XO_list)
        play = 1

    else:
        XO_list = takeInput(1, XO_list)
        printBoard(XO_list)
        gameStatus = checkWin(XO_list)
        play = 0