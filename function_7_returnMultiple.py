## Programm 7 - to understand how a function returns two values

# a function that returns two results 

def sum_sub(a, b):
    """ this function returns results of 
    addition and subtraction of a, b """
    
    c = a + b 
    d = a - b 
    
    return c, d
    
    
# call function and get the results from sum_sub() function 
x, y = sum_sub(10, 5)

# display the results
print("Result of addition :", x)
print("Result f subtraction :", y)



# Output:
'''
F:\PY>py function_7_returnMultiple.py
Result of addition : 15
Result f subtraction : 5
'''