# 7.Please write a program which count and print the numbers of each character in a string input by console.

# Example: If the following string is given as input to the program:abcdefgabc

# Then, the output of the program should be:
'''
a,2
c,2
b,2
e,1
d,1
g,1
f,1
'''

str = input('Enter a string :')
#ch = list(str)
#print(ch)

# take an empty Dictionary
d = {}

# store into d each letter as key and it's number of occurrences as value

for i in str:
    d[i] = d.get(i, 0) + 1
    # get() method - it says if 'i' (this is a letter of the string) is found in dictionary 'd', then return it's value; else return 0 
    # But we have added '1' to the value returned by get() method, and jence, if 'i' is not found, it returns 1.
    # if 'i' is found then it returns the value of i' plus 1


# display the key n value pairs in dictionary

for k, v in d.items():
    print('{},{}'.format(k, v))




# Output:
"""
F:\PY\Module1\CaseStudy_1>py demo7.py
Enter a string :hello
h,1
e,1
l,2
o,1

F:\PY\Module1\CaseStudy_1>py demo7.py
Enter a string :abcdefgabc
a,2
b,2
c,2
d,1
e,1
f,1
g,1

F:\PY\Module1\CaseStudy_1>
"""


'''
F:\PY\Module1\CaseStudy_1>py demo7.py
Enter a string :hello
['h', 'e', 'l', 'l', 'o']
h 1
e 1
l 2
l 2
o 1

F:\PY\Module1\CaseStudy_1>
'''

