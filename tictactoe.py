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
        print("1")
        winner = True
    elif (board['4'] == board['5'] == board['6']) and board['4'] != ' ':
        print(board['4'] + " Wins!")
        print("2")
        winner = True
    elif (board['7'] == board['8'] == board['9']) and board['7'] != ' ':
        print(board['7'] + " Wins!")
        print("3")
        winner = True
    elif (board['1'] == board['4'] == board['7']) and board['1'] != ' ':
        print(board['1'] + " Wins!")
        print("4")
        winner = True
    elif (board['2'] == board['5'] == board['8']) and board['2'] != ' ':
        print(board['2'] + " Wins!")
        print("5")
        winner = True
    elif (board['3'] == board['6'] == board['9']) and board['3'] != ' ':
        print(board['3'] + " Wins!")
        print("6")
        winner = True
    elif (board['1'] == board['5'] == board['9']) and board['1'] != ' ':
        print(board['1'] + " Wins!")
        print("7")
        winner = True
    elif (board['3'] == board['5'] == board['7']) and board['3'] != ' ':
        print(board['3'] + " Wins!")
        print("8")
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
    while counter < 9:
        printBoard()
        move = input()

        if board[move] == ' ':
            counter += 1
            board[move] = symbol
        else:
            print("That spot is already taken!")
        if counter >= 5:
            winner = checkWinner()
        if winner:
            printBoard()
            break
        if symbol == 'x':
            symbol = 'o'
        else:
            symbol = 'x'
    if counter == 9 & winner == False:
        print("Its a tie!")

def main():
    playGame()
    playAgain = input("Would you like to play again?(Y/N)\n")
    while playAgain == 'Y' or playAgain == 'y':
        clearBoard()
        playGame()
        playAgain = input("Would you like to play again?(Y/N)\n")

    print("Thank you for playing!")

main()
