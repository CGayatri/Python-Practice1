## program 24 - to display numbers from 10 to 6 and break the loop when the number abut to display  is 5.

# Using break to come out of loop - while loop 

x = 10

while (x >= 1):
    if (x == 5):
        break
    
    print('x =', x)
    x-=1
    
print('Out of loop')


'''
F:\PY>py control_24.py
x = 10
x = 9
x = 8
x = 7
x = 6
Out of loop
'''

x = 10
br = int(input('Enter number between 1 to 10 to halt loop : '))
while (x >= 1):
    if (x == br):
        break
    
    print('x =', x)
    x-=1
    
print('Out of loop')


'''
F:\PY>py control_24.py
Enter number between 1 to 10 to halt loop : 7
x = 10
x = 9
x = 8
Out of loop

F:\PY>py control_24.py
Enter number between 1 to 10 to halt loop : 2
x = 10
x = 9
x = 8
x = 7
x = 6
x = 5
x = 4
x = 3
Out of loop
'''


"""
F:\PY>py control_24.py
x = 10
x = 9
x = 8
x = 7
x = 6
Out of loop
Enter number between 1 to 10 to halt loop : 4
x = 10
x = 9
x = 8
x = 7
x = 6
x = 5
Out of loop
"""