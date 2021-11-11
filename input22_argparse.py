## program - 22 : to find the power value of a number when it is rised to a particular power 

import argparse

# call the ArgumentParser()
parser = argparse.ArgumentParser()

# add the arguments to teh parser 
parser.add_argument('nums', nargs=2)

# retrieve arguments from parser 
args = parser.parse_args()

#find the power value 
#args.nums is a list 
print("Number =", args.nums[0])
print("It\'s power =", args.nums[1])

# calculate power by coverting strings to numbers 
result = float(args.nums[0]) ** float(args.nums[1])

print("power rsult = ", result)


"""
F:\PY>py input22_argparse.py 10.5 3
Number = 10.5
It's power = 3
power rsult =  1157.625
"""