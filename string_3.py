## program 3 - to know whether a sub string exists in main string or not

str = input("Enter a main string: ")
sub = input("Enter a sub string: ")

"""
if sub in str:
    print(sub + ' is found in main string')
else: 
    print(sub + ' is not found in the main string')
"""

'''
F:\PY>py string_3.py
Enter a main string: Hello
Enter a sub string: Hell
Hell is found in main string

F:\PY>py string_3.py
Enter a main string: Hello
Enter a sub string: hell
hell is not found in the main string

F:\PY>py string_3.py
Enter a main string: 12345
Enter a sub string: 23
23 is found in main string

F:\PY>py string_3.py
Enter a main string: Orange
Enter a sub string: Mango
Mango is not found in the main string

F:\PY>py string_3.py
Enter a main string: Mango
Enter a sub string:
 is found in main string

'''


if sub not in str:
    print(sub + ' is not found in the main string')
else:
    print(sub + ' is found in main string')
    
'''
F:\PY>py string_3.py
Enter a main string: Hello
Enter a sub string: hell
hell is not found in the main string

F:\PY>py string_3.py
Enter a main string: Hello
Enter a sub string: Hell
Hell is found in main string

F:\PY>py string_3.py
Enter a main string: Orange
Enter a sub string:
  is not found in the main string

F:\PY>py string_3.py
Enter a main string:
Enter a sub string:
 is found in main string

F:\PY>py string_3.py
Enter a main string: Mango
Enter a sub string:
 is found in main string

F:\PY>
'''