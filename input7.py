## program - 7 : to accept two integer numbers from keyboard 

x = int(input('Enter first number: ') )
y = int(input('Enter second number: '))


#print('U entered: ', x, y)


'''
F:\PY>py input7.py
Enter first number: 12
Enter second number: 34
U entered:  12 34
'''

#print('U entered: ', x, y, sep=',')
#U entered: ,12,34

print('U entered: %d, %d' %(x, y))
#U entered: 12, 34