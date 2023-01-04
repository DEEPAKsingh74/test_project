#!/usr/bin/python3

import colorama
import pyfiglet

"""
DOCSTRING :  This project lets you print the table till the number specified by the user. 
"""

colorama.init()
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
cy = '\033[095m'
cya = '\033[095m'


def printMultiplicationTable(num):
    print(red)
    print("-" * 100)
    print("-" * 100)
    result = pyfiglet.figlet_format("  TABLE OF    {}  ".format(num))
    print(result)
    print("-" * 100)
    print("-" * 100)
    for j in range(1, 11, 1):
        print(green, num, red, "*", cyan, j, yellow, "=", cya, num * j)
    print()


class multiplicationTable:
    def __init__(self, __number):
        self.number = number

    def callMultiplicationTable(self):
        for i in range(2, self.number + 1, 1):
            printMultiplicationTable(i)


if __name__ == "__main__":
    print(yellow)
    number = int(input("Enter the range of table you want : "))
    obj = multiplicationTable(number)
    obj.callMultiplicationTable()
