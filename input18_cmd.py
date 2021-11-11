## program - 18 : to find ssum of two numbers using command line arguments

# to add two numbers
import sys
#from sys import argv 

# convert args into integres and add them 
sum = int(sys.argv[1]) + int(sys.argv[2])
print("Sum = ",sum)

'''
F:\PY>py input18_cmd.py 10 22
Sum =  32
'''


"""
F:\PY>py input18_cmd.py
Traceback (most recent call last):
  File "input18_cmd.py", line 7, in <module>
    sum = int(sys.argv[1]) + int(sys.argv[2])
IndexError: list index out of range

"""