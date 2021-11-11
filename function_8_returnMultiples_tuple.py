## Program 8 - returns results of addition, subtraction, multiplication, and division 
# function returns several result in a tuple 

def sum_sub_mul_div(a, b):
    """ this function returns results of addition,
        subtraction, multiplication and division of a,b """
    
    c = a + b 
    d = a - b 
    e = a * b 
    f = a / b 

    return c, d, e, f
    
    
# call function and get teh results from sum_sub_mul_div() function and store into tuple t 
t = sum_sub_mul_div(10, 5)
print('t =', t)

# display the results using for loop 
print('The reslts are : \n')
for i in t :
    print(i, end=', ')
    
    


#Output :
'''
F:\PY>py function_8_returnMultiples_tuple.py
t = (15, 5, 50, 2.0)
The reslts are :

15, 5, 50, 2.0,
F:\PY>
'''