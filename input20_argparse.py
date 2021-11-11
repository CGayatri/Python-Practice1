## parsing command line arguments

## program - 20 : Using argument parser to find the square of a given number 

# to find square of a given number, 

import argparse
#from argparse imprt ArgumentParser

# create ArgumentParser class object for displaying a help 
parser =  argparse.ArgumentParser(description='This program displays a square value of given number')

# add one value with name 'num' and typ as integer 
parser.add_argument("num", type=int, help="Please input integer type number only.") 

# retrieve the arguments passed to the program 
args = parser.parse_args()

print(args)

# find square of the argument passed
result = args.num ** 2

print("Square of {0} is = {1}".format(args.num, result))



"""
F:\PY>py input20_argparse.py 5
Namespace(num=5)
Square of 5 is = 25
"""

'''
F:\PY>py input20_argparse.py 5.5
usage: input20_argparse.py [-h] num
input20_argparse.py: error: argument num: invalid int value: '5.5'
'''

'''
F:\PY>py input20_argparse.py 5 15
usage: input20_argparse.py [-h] num
input20_argparse.py: error: unrecognized arguments: 15
'''

'''
F:\PY>py input20_argparse.py
usage: input20_argparse.py [-h] num
input20_argparse.py: error: the following arguments are required: num
'''

'''
F:\PY>py input20_argparse.py -h
usage: input20_argparse.py [-h] num

This program displays a square value of given number

positional arguments:
  num         Please input integer type number only.

optional arguments:
  -h, --help  show this help message and exit
'''