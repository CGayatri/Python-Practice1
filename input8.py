## program - 8 : to accept two numbers and find their sum 

x = int(input('Enter first number : '))
y = int(input('Enter second number : '))

#print('The sum of', x, ' and ', y, ' is :', x, y, (x+y))

'''
F:\PY>py input8.py
Enter first number : 200
Enter second number : 300
The sum of 200  and  300  is : 200 300 500
'''

print('The sum of {} and {} is : {}'.format(x,y,(x+y)))

"""
F:\PY>py input8.py
Enter first number : 200
Enter second number : 300
The sum of 200 and 300 is : 500
"""

#print('The sum of {} and {} is : {0}'.format(x,y,(x+y)))  #-- generates error 
'''
    print('The sum of {} and {} is : {0}'.format(x,y,(x+y)))
ValueError: cannot switch from automatic field numbering to manual field specification
'''