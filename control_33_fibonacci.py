## program 33 - to generate Fibonacci number series

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, etc.


n = int(input('How many Fibonacci numbers?: '))

f1 = 0      # this is firt Fibonacci no
f2 = 1      # this is second one

c = 2       # counts no. of Fibonaccis , starts with 2 cuz first two are not included in loop ; first two numbers are for sure gonna get printed. 
            # hence, total count should be = n-2

if (n == 1):
    print(f1)
elif (n == 2):
    print(f1, '\n', f2, sep='')
else:
    print(f1, '\n', f2, sep='')
    
    while c<n :
        f = f1+f2       # add two Fibnaccis to get the next one 
        print(f)
        f1 = f2
        f2 = f
        c+=1            # increment counter


'''
F:\PY>py control_33_fibonacci.py            ====== c=0
How many Fibonacci numbers?: 10
0
1
1
2
3
5
8
13
21
34
55
89

F:\PY>py control_33_fibonacci.py            ====== c = 2
How many Fibonacci numbers?: 10
0
1
1
2
3
5
8
13
21
34

F:\PY>
''' 