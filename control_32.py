## program 32 - to display prime number series 

# program to print prime numbers upto a given number

# accept upto what number the user wants 

max = int(input("Upto what number? "))

for num in range(2, max+1):         # generate from 2 onwards till max
    for i in range(2,num) :         # i represents numbers from 2 to num-1
        if (num % i) == 0:          # if num is divisible by i
            break                   # then it is not prime, hence go back and check next number 
    else :
        print(num)            # otherwise it is prime and hence display 
        

"""
F:\PY>py control_32.py
Upto what number? 30
2
3
5
7
11
13
17
19
23
29

F:\PY>
"""

"""
F:\PY>py control_32.py
Upto what number? 10
2
3
5
7

F:\PY>
"""


'''
F:\PY>py control_32.py
Upto what number? 30
3
5
5
5
7
7
7
7
7
9
11
11
11
11
11
11
11
11
11
13
13
13
13
13
13
13
13
13
13
13
15
17
17
17
17
17
17
17
17
17
17
17
17
17
17
17
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
21
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
25
25
25
27
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
'''