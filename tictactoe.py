import sys
import math
import threading
import time
import random
from functools import reduce


board = {'1':' ', '2':' ', '3':' ',
        '4': ' ','5':' ','6':' ',
        '7': ' ','8':' ','9':' '}

def checkWinner():
    winner = False
    if (board['1'] == board['2'] == board['3']) and board['1'] != ' ':
        print(board['1'] + " Wins!")
        winner = True
    elif (board['4'] == board['5'] == board['6']) and board['4'] != ' ':
        print(board['4'] + " Wins!")
        winner = True
    elif (board['7'] == board['8'] == board['9']) and board['7'] != ' ':
        print(board['7'] + " Wins!")
        winner = True
    elif (board['1'] == board['4'] == board['7']) and board['1'] != ' ':
        print(board['1'] + " Wins!")
        winner = True
    elif (board['2'] == board['5'] == board['8']) and board['2'] != ' ':
        print(board['2'] + " Wins!")
        winner = True
    elif (board['3'] == board['6'] == board['9']) and board['3'] != ' ':
        print(board['3'] + " Wins!")
        winner = True
    elif (board['1'] == board['5'] == board['9']) and board['1'] != ' ':
        print(board['1'] + " Wins!")
        winner = True
    elif (board['3'] == board['5'] == board['7']) and board['3'] != ' ':
        print(board['3'] + " Wins!")
        winner = True

    return winner


def printBoard():
    for i in board:
        print(board[i]+"|", end="")
        if int(i)%3 == 0:
            print()

def clearBoard():
    for i in board:
        board[i] = ' '

def playGame():
    counter = 0
    symbol = 'x'
    winner = False
    validMove = False
    while counter < 9:
        printBoard()
        move = input()

        if board[move] == ' ':
            counter += 1
            board[move] = symbol
            validMove = True
        else:
            print("That spot is already taken!")
            validMove = False
        if counter >= 5:
            winner = checkWinner()
        if winner:
            printBoard()
            break
        if symbol == 'x' and validMove:
            symbol = 'o'
        elif symbol == 'o' and validMove:
            symbol = 'x'
    if counter == 9 & winner == False:
        print("Its a tie!")

def main():
    playGame()
    while True:
        playAgain = input("Would you like to play again?(Y/N)\n")
        if playAgain == 'Y' or playAgain == 'y':
            clearBoard()
            playGame()
        else:
            break

    print("Thank you for playing!")

main()
