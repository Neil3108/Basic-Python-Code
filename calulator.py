import sys
import math
import threading
import time
from functools import reduce

a = input("Enter the first number: ") # First number
b = input("Enter the second number: ") # Second number

c = input("Enter operations (+,-,*,/,**): ") # Operation input

match c:
    case "+":
        print(int(a)+int(b))
    case "-":
        print(int(a) - int(b))
    case "*":
        print(int(a) * int(b))
    case "/":
        print(float(a) / float(b))
    case "**":
        print(int(a) ** int(b))
    case _:
        print("Wrong input.")
