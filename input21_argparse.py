## program - 21 : to add two numbers using argument parser 

import argparse 

# create ArgumentParser class object with help message
parser = argparse.ArgumentParser(description = "This program calculates sum of  two given numbers")

# add two arguments wih the names n1 and n2 and type as float 
parser.add_argument("n1", type=float, help="Input first number") 
parser.add_argument("n2", type=float, help="Input second number")

# retrieve the arguments passed to the program 
args = parser.parse_args()

# convert n1 and n2 to float and then add them
result = float(args.n1) + float(args.n2)

print("Sum of two =", result)



'''
F:\PY>py input21_argparse.py
usage: input21_argparse.py [-h] n1 n2
input21_argparse.py: error: the following arguments are required: n1, n2
'''

"""
F:\PY>py input21_argparse.py 10.5 15
Sum of two = 25.5
"""