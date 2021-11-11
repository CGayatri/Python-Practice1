# 5.Please   write   a   program   which   accepts  a   string   from   console   and   print   the characters that have even indexes.

# Example: If the following string is given as input to the program:
	# H1e2l3l4o5w6o7r8l9d
	# Then, the output of the program should be:
	# Helloworld
    

str = input("Enter input string : ")
str = str[0: len(str) : 2]    

print(str)

'''
F:\PY\Module1\CaseStudy_1>py demo5.py
Enter input string : H1e2l3l4o5w6o7r8l9d
Helloworld

F:\PY\Module1\CaseStudy_1>
'''
