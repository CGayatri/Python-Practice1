## program - 23 : To accept one or more arguments and display them as a list elements 

import argparse 

# call teh ArgumentParser()
parser = argparse.ArgumentParser();

# add arguments to teh parser 
parser.add_argument("nums", nargs='+')
#parser.add_argument("nums", nargs=*)

# retrieve the arguments into args object 
args = parser.parse_args();

# display as a list 
for x in args.nums:
    print(x)



"""

F:\PY>py input23_argparse.py
usage: input23_argparse.py [-h] nums [nums ...]
input23_argparse.py: error: the following arguments are required: nums

F:\PY>py input23_argparse.py 10 Gayatri 78.5
10
Gayatri
78.5

"""