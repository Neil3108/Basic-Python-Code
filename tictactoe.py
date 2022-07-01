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
    if board['1'] == board['2'] == board['3']:
        print(board['1'] + " Wins!")
        winner = True
    elif board['4'] == board['5'] == board['6']:
        print(board['4'] + " Wins!")
        winner = True
    elif board['7'] == board['8'] == board['9']:
        print(board['7'] + " Wins!")
        winner = True
    elif board['1'] == board['4'] == board['7']:
        print(board['1'] + " Wins!")
        winner = True
    elif board['2'] == board['5'] == board['8']:
        print(board['2'] + " Wins!")
        winner = True
    elif board['3'] == board['6'] == board['9']:
        print(board['3'] + " Wins!")
        winner = True
    elif board['1'] == board['5'] == board['9']:
        print(board['1'] + " Wins!")
        winner = True
    elif board['3'] == board['5'] == board['7']:
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
    while counter < 9:
        printBoard()
        move = input()
        counter += 1

        if board[move] == ' ':
            board[move] = symbol
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
    while playAgain == 'Y':
        clearBoard()
        playGame()
        playAgain = input("Would you like to play again?(Y/N)\n")

main()
