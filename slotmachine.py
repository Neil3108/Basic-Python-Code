import sys
import math
import threading
import time
import random
from functools import reduce

def getSymbols():
    numSymbol = int(input("Enter the number of symbols: ").strip())
    symbolList = []
    counter = 0
    while True:
        if numSymbol <= 0:
            print("The number of symbols must be greater than 0")
            numSymbol = input("Enter the number of symbols: ")
        else:
            break
    while counter < numSymbol:
        symbol = input("Enter 1 symbol: ")
        symbolList.append(symbol)
        counter += 1

    return symbolList


# Generates sequences for 3 symbols
def generateSequences(symbols):
    sequences = []
    for symbols0 in symbols:
        for symbols1 in symbols:
            for symbols2 in symbols:
                sequences.append(symbols0 + symbols1 + symbols2)
    return sequences

def displaySequences(sequences):
    print("\nThe sequences of symbols are:")
    for sequence in sequences:
        print(sequence)

def countWinners(sequences):
    countWinners = 0
    for sequence in sequences:
        if sequence[0] == sequence[1] and sequence[1] == sequence[2]:
            countWinners += 1
    return countWinners


def main():
    symbols = getSymbols()
    sequences = generateSequences(symbols)
    displaySequences(sequences)
    winners = countWinners(sequences)

    print("There are %d winning sequences out of %d total sequences." % (winners, len(sequences)))

main()
