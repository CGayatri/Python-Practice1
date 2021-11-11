## program 25 - to display numbers from 1 to 5 using continue statement 

x = 0;

while (x < 10):
    x+=1
    if (x>5):           # if x>5 then continue next iteration 
        continue
    print('x =', x)
print('Out of loop')



'''
F:\PY>py control_25.py
x = 1
x = 2
x = 3
x = 4
x = 5
Out of loop
'''