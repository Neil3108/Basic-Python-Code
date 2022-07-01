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
    if board['1'] == board['2'] == board['3']:
        print(board['1'] + "Wins!")
    elif board['4'] == board['5'] == board['6']:
        print(board['4'] + "Wins!")
    elif board['7'] == board['8'] == board['9']:
        print(board['7'] + "Wins!")
    elif board['1'] == board['4'] == board['7']:
        print(board['1'] + "Wins!")
    elif board['2'] == board['5'] == board['8']:
        print(board['2'] + "Wins!")
    elif board['3'] == board['6'] == board['9']:
        print(board['3'] + "Wins!")
    elif board['1'] == board['5'] == board['9']:
        print(board['1'] + "Wins!")
    elif board['3'] == board['5'] == board['7']:
        print(board['3'] + "Wins!")

def main():


main()
