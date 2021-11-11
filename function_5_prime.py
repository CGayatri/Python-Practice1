## Program 5 - to check whether a given number is prime or not 

def prime(num):
    """ to check if num is prime or not """
    
    flag = 1            # this is 1 --> prime; 0 --> not prime 
    
    for i in range(2, n):       # any number is divisible by 1 n self; so exclude those . i.e. consider 2 to (n-1) numbers as dividers 
        if (n % i == 0 ):
            flag = 0
            break               #Most important to break once number is decided as not prime; even once divisible, no need to check further for that number 
            
        else : 
            flag = 1
    
    #return flag 
    # test flag to decide prime or not : 1 - prime , 0- not prime 
    if flag == 1:
        print(num, ' is prime')
    else :
        print(num, ' is not prime')
    
'''  
# test flag to decide prime or not : 1 - prime , 0- not prime 
if flag == 1:
    print(num, ' is prime')
else :
    print(num, ' is not prime')
'''


# test if a number passed is prime or not 

n = int(input('Enter a number : '))
prime(n)

    
    
#Output : 
'''
F:\PY>py function_5_prime.py
Enter a number : 5
5  is prime

F:\PY>py function_5_prime.py
Enter a number : 18
18  is not prime

F:\PY>py function_5_prime.py
Enter a number : 567893
567893  is not prime

F:\PY>py function_5_prime.py
Enter a number : 11111
11111  is not prime

F:\PY>py function_5_prime.py
Enter a number : 111111
111111  is not prime

F:\PY>py function_5_prime.py
Enter a number : 3547589
3547589  is not prime

F:\PY>py function_5_prime.py
Enter a number : 53
53  is prime

F:\PY>
'''
