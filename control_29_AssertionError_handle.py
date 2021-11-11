## program 29 - to handle the AssertionError exception thats is given by assert statement 

# handle an exception using 'try ... except' statements 

num = int(input('Enter a number greeater than 0: '))

try:
    assert num>0, 'Wrong input entered, number should be greater than 0'    # Exception may occur here
except AssertionError:
    print("Wrong input entered, number should be greater than 0")           # this is exected in case of exception 

print('U entered :', num)


'''
F:\PY>py control_29_AssertionError_handle.py
Enter a number greeater than 0: 5
U entered : 5

F:\PY>py control_29_AssertionError_handle.py
Enter a number greeater than 0: -4
Wrong input entered, number should be greater than 0
U entered : -4

F:\PY>
'''