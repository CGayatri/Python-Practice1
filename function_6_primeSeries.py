## Program 6 - generates a series of prime numbers with teh help of a function to test prime or not 

# a function to test whether a number is prime or not 

def prime(n):
    """ to check if n is prime or not """
    
    flag = 1        # this will be 0 --> if no prime 
    for i in range(2, n):
        if (n%i == 0):
            flag = 0
            break       #Most important to break once number is decided as not prime; even once divisible, no need to check further for that number 
        else :
            flag = 1
            
    return flag
 
 
# Generate pime number series

num = int(input('How many primes do you want? : ')) 

# start with value 2 
i = 2

# count - no of primes (0 to 9 == 10 )
count = 0

while True:         # repeat forever     
    if prime(i):    # if True - if i is prime, display it
        print(prime(i), i)
        count+=1    # increse counter , to check later whether displayed primes are not exceeding given limit fo series 
    
    i+=1            # generate next number to test 

    if count >= num:     # if count exceeds num , then break here and come out of loop  
        break
        

#Output:
'''
F:\PY>py function_6_primeSeries.py
How many primes do you want? : 10
1 2
1 3
1 5
1 7
1 11
1 13
1 17
1 19
1 23
1 29

F:\PY>
'''