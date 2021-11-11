## program 19 - program that displays stars in right angled triangular form using nested loops

rows = 10
cols = rows

for i in range(1, rows+1):
    for j in range(1, i+1):
        print('* ', end='')
    print() 
    
    
'''
F:\PY>py control_19.py
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
* * * * * * * * * *

'''