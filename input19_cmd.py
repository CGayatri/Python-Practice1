## program - 19 : to find sum of even numbers from command line arguments 

import sys
#from sys import argv 

# read command line arguments exept the program name 
args = sys.argv[1:]     #slicing operator from 1st element onwards till end 
print(args)

# find sum of even arguments 
sum = 0 
for a in args:
    i = int(a)          #convert string to integer 
    if (i % 2 == 0 ):
        sum+=i
        
print("Sum of evens =", sum)


"""
F:\PY>py input19_cmd.py 6 8 9 10 11
['6', '8', '9', '10', '11']
Sum of evens = 24
"""

