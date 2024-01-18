# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Olurotimi Ajayi"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101253689"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-22"

#==========================================#
# Place your script for your batch_UI after this line

from load_data import *
from sort import *
from histogram import *
from curve_fit import *

number1 = 'L'
number2 = 'S'
number3 = 'C'
number4 = 'H'
number5 = 'E'


command1 = input('Please enter the name of the file where your commands are stored: ')
with open(command1, 'r') as file:
    commands_in_file = file.read().split('\n')



for command in commands_in_file:
    command = command.split(';')
    if command[0] == 'L':
        run = load_data(command[1], (command[2], command[3]))
        average = add_average(run)
    if command[0] == 'S':
        random = sort_by_key(run, 'A', command[1])
        if command[2] == 'Y':
            print(random)
    if command[0] == 'H':
        hist = histogram(run, command[1])
    if command[0] == 'C':
        curve = curve_fit(average, command[1], int(command[2]))
        print(curve)

