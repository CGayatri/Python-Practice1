## program 6 - to test whether a given number is in between 1 and 10


x = int(input("Enter a number: "))

# compound condition
if (x>=1 and x<=10):
    print("You typed", x, "which is between 1 and 10")
else :
    print("You typed", x, "which is below 1 or above 10")
    
    
'''
F:\PY>py control_6.py
Enter a number: 2345
You typed 2345 which is below 1 or above 10

F:\PY>py control_6.py
Enter a number: 6
You typed 6 which is between 1 and 10

F:\PY>py control_6.py
Enter a number: -9
You typed -9 which is below 1 or above 10

'''