## program - 17 : to dispaly command line arguments

import sys 
#from sys import argv 

n = len(sys.argv)       # n is the number of arguments / length 
args = sys.argv         # args list contains arguments 
print('Number of command line arguments =', n)

print('The arguments are :', args)
print()

print('The arguments one by one : ')
for a in args:
    print(a)


"""
F:\PY>py input17_cmd.py
Number of command line arguments = 1
The arguments are : ['input17_cmd.py']

The arguments one by one :
input17_cmd.py
'''


'''
F:\PY>py input17_cmd.py 10 Aishwarya Rai 22500.75
Number of command line arguments = 5
The arguments are : ['input17_cmd.py', '10', 'Aishwarya', 'Rai', '22500.75']

The arguments one by one :
input17_cmd.py
10
Aishwarya
Rai
22500.75

"""

"""
F:\PY>py input17_cmd.py 10 "Aishwarya Rai" 22500.75
Number of command line arguments = 4
The arguments are : ['input17_cmd.py', '10', 'Aishwarya Rai', '22500.75']

The arguments one by one :
input17_cmd.py
10
Aishwarya Rai
22500.75
"""


'''
F:\PY>py input17_cmd.py 10 "'Aishwarya Rai'" 22500.75
Number of command line arguments = 4
The arguments are : ['input17_cmd.py', '10', "'Aishwarya Rai'", '22500.75']

The arguments one by one :
input17_cmd.py
10
'Aishwarya Rai'
22500.75

F:\PY>py input17_cmd.py 10 '"Aishwarya Rai"' 22500.75
Number of command line arguments = 4
The arguments are : ['input17_cmd.py', '10', "'Aishwarya Rai'", '22500.75']

The arguments one by one :
input17_cmd.py
10
'Aishwarya Rai'
22500.75

F:\PY>
'''