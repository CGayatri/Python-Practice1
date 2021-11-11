## Program 2 - to find sum of two numbers and return the result from the function

# a function to add two numbers 

def sum(a, b):
    """ This function finds sum of two numbers """
    c = a + b 
    return c        # return result 
    
    
# call the function which returns a value 
x = sum(10, 15)
print('The sum is :', x)

y = sum(1.5, 10.75)
print('The sum is :', y)

#Output:
'''
F:\PY>py function_2.py
The sum is : 25
The sum is : 12.25
'''