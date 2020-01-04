import math
import turtle
import numpy
import random
from pandas import *

#main starts the engine up
def main():
    board_generator()


#generates a random board state with a unique possible solution from a given text file
def board_generator():
    #parse through the text file
    lines = open("C:\\Users\\Bomin\\PycharmProjects\\SudokuEngine\\HardTestCases.txt").readlines()
    #choose random line within file
    line = lines[random.randint(0,2365)]
    #split the parsed line into a string then into array
    parsed_line = line.split()
    parsed_string = parsed_line[0]
    parsed_array = []
    parsed_array[:0] = parsed_string
    #parse through the single array and turn it into 2d array
    board = []
    n = 0
    for rows in range(0,9):
        sub = []
        for col in range(0,9):
            if(parsed_array[n] == '.'):
                sub.append(0)
            else:
                sub.append(int(parsed_array[n]))
            n += 1
        board.append(sub)

    print(DataFrame(board))

# def __init__(self)

main()
