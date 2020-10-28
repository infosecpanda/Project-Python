# My First Milestone Project in Python
# Created by: Aishwarya Iyer
# Date: 28/10/20
# Welcome to Tic Tac Toe

import random
#Asking to play
def get_answer():
    answer='no'
    while(answer != 'yes'):
        answer=input("Do you want to play? ")
    return answer

#This function will assign 'X' and '0' to Player 1 and Player 2 respectively
def assign_marker():
    marker='p'
    while (marker != 'X' and marker != '0'):
        marker=input("Player 1, Do you want to be X or 0?")
    if(marker=='X'):
        return('X','0')
    else:
        return('0','X')


#This function will randomly choose the first player 
def choose_first():
    if random.randint(0, 1) == 0:
        print("Player 2 goes first")
        return 'Player 2'
    else:
        print("Player 1 goes first")
        return 'Player 1'

#Displaying the board with respective positional values
def display_board(board):
    print("   "+"|"+"   "+"|"+"   ")
    print(" "+board[7]+" "+"|"+" "+board[8]+" "+"|"+" "+board[9]+" ")
    print("   "+"|"+"   "+"|"+"   ")
    print("-----------")
    print("   "+"|"+"   "+"|"+"   ")
    print(" "+board[4]+" "+"|"+" "+board[5]+" "+"|"+" "+board[6]+" ")
    print("   "+"|"+"   "+"|"+"   ")
    print("-----------")
    print("   "+"|"+"   "+"|"+"   ")
    print(" "+board[1]+" "+"|"+" "+board[2]+" "+"|"+" "+board[3]+" ")
    print("   "+"|"+"   "+"|"+"   ")

#This function will prompt for the positional value from the player to place their marker
def assign_to_board():
    positional_value=-1
    while(positional_value not in range(0,10)):
        positional_value=int(input("Enter a positional value from 1-9"))
    return positional_value

#This function will check if the positional value entered by the player has already been assigned
def space_check(board,positional_value):
    if(board[positional_value]=='X' or board[positional_value]=='0'):
        return False
    return True

#Checking if any of the player's marker('X' or '0') has won
def win_check(board,marker):
    win=False
    if((board[1]==marker and board[2]==marker and board[3]==marker) or 
    (board[4]==marker and board[5]==marker and board[6]==marker) or 
    (board[7]==marker and board[8]==marker and board[9]==marker) or 
    (board[1]==marker and board[4]==marker and board[7]==marker) or 
    (board[2]==marker and board[5]==marker and board[8]==marker) or 
    (board[3]==marker and board[6]==marker and board[9]==marker) or 
    (board[1]==marker and board[5]==marker and board[9]==marker) or 
    (board[3]==marker and board[5]==marker and board[7]==marker)):
        return True

#Function to check if all the spaces in the board has filled to call it a draw
def full_board_check(board):
    i=1
    for i in range(1,10):
        if(space_check(board,i)):
            return False
    return True

#Main funtion
def play():
    if(get_answer()=='yes'):
        print("Welcome to Tic Tac Toe")
    board=['0','1','2','3','4','5','6','7','8','9']
    game_on=True
    player1_marker,player2_marker=assign_marker()
    turn=choose_first()
    #player1
    while(game_on==True):
        if(turn=='Player 1'):
            display_board(board)
            positional_value=assign_to_board()
            #If the positional vaue has already been assigned
            if(space_check(board,positional_value)== False):
                print("Position Taken")

            #If the positional value has not been assigned, the player's marker gets assigned    
            else:
                board[positional_value]=player1_marker
                turn='Player 2'
            if(win_check(board,player1_marker)):
                display_board(board)
                print("Player 1 has won")
                game_on=False

            #Checking if it's a Draw
            elif(full_board_check(board)):
                print("It's a draw!!")
                game_on=False
                display_board(board)
                
        else:
            turn='Player 2'
    #player2
        if(turn=='Player 2'):
            display_board(board)
            positional_value=assign_to_board()
            #If the positional vaue has already been assigned
            if(space_check(board,positional_value)==False):
                print("Position Taken")

            #If the positional value has not been assigned, the player's marker gets assigned    
            else:
                board[positional_value]=player2_marker
                turn='Player 1'
            if(win_check(board,player2_marker)):
                display_board(board)
                print("Player 2 has won")
                game_on=False

            #Checking if it's a Draw
            elif(full_board_check(board)):
            	print("It's a draw!!")
                game_on=False
                display_board(board)
           		
                
        else:
            turn='Player 1'


play()
