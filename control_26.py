## program 26 - to know 'pass' does nothing 

# using pass to do nothing 

x = 0
while x < 10:
    x+=1 
    if x>5 :
        pass
    print('x =', x)

print("Out of loop")


'''
F:\PY>py control_26.py
x = 1
x = 2
x = 3
x = 4
x = 5
x = 6
x = 7
x = 8
x = 9
x = 10
Out of loop
'''