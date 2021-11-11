## program - 12 : to accept 3 integers separated by comma and diaplay thir sum 

# accepting 3 numbers separated by comma

num1, num2, num3 = [int(i) for i in input('Enter three numbers comma separated : ').split(',')]

print('The sum of numbers {0}, {1}, {2} is = {3}'.format(num1, num2, num3, (num1+num2+num3)))

'''
F:\PY>py input12.py
Enter three numbers comma separated : 10, 20, 30
The sum of numbers 10, 20, 30 is = 60
'''