## Program 4 - to calculate factorial numbers 

def fact(n):
    """ to find factorial value of n """
    prod = 1
    while (n >= 1):
        prod = prod * n
        n = n-1
        
    return prod
    
    
# display factorials of first 10 numbers 
# call fact() function and pass the numbers from 1 to 10 

for i in range(1, 11):

    print('Factorial of {} is {}'.format(i,  fact(i)))
  
#Output:
"""
F:\PY>py function_4_fact.py
Factorial of 1 is 1
Factorial of 2 is 2
Factorial of 3 is 6
Factorial of 4 is 24
Factorial of 5 is 120
Factorial of 6 is 720
Factorial of 7 is 5040
Factorial of 8 is 40320
Factorial of 9 is 362880
Factorial of 10 is 3628800
"""  

'''
1
2
6
24
120
720
5040
40320
362880
3628800
'''