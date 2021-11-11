## program - 9 : to find sum and product of two numbers 


x = int(input('Enter first number : '))
y = int(input('Enter second number : '))

print('The sum of {0} and {1} is {2}'.format(x, y, (x+y)))
print('The product of {0} and {1} is {2}'.format(x, y, (x*y)))

'''
F:\PY>py input9.py
Enter first number : 20
Enter second number : 30
The sum of 20 and 30 is 50
The product of 20 and 30 is 600
'''

#print('The sum of {1} and {2} is {3}'.format(x, y, (x+y)))
#IndexError: Replacement index 3 out of range for positional args tuple


print('The sum of {0} and {1} is {2} and product of {0} and {1} is {3}'.format(x, y, (x+y), (x*y)))

'''
The sum of 20 and 30 is 50 and product of 20 and 30 is 600
'''