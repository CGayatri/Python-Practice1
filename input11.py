## program - 11 : to accept 3 integers in the same line and diaplay thir sum 

# accepting 3 numbers separated by space

num1, num2, num3 = [int(i) for i in input('Enter three numbers space separated : ').split()]

print('The sum of numbers {0}, {1}, {2} is = {3}'.format(num1, num2, num3, (num1+num2+num3)))

'''
F:\PY>input11.py
Enter three numbers space separated : 23 34 45
The sum of numbers 23, 34, 45 is = 102
'''
