## program 8 - to accept a numeric digit from keyboard and display in words

x = int(input('Enter a digit: '))

if (x==0): print("ZERO")
elif (x==1): print("ONE")
elif (x==2): print("TWO")
elif (x==3): print("THREE")
elif (x==4): print("FOUR")
elif (x==5): print("FIVE")
elif (x==6): print("SIX")
elif (x==7): print("SEVEN")
elif (x==8): print("EIGHT")
elif (x==9): print("NINE")      # else part is not compulsory

#else : print("Please enter a digit between 0 and 9")


"""
F:\PY>py control_8.py
Enter a digit: 23

F:\PY>py control_8.py
Enter a digit: 5
FIVE

F:\PY>py control_8.py
Enter a digit: 4.5
Traceback (most recent call last):
  File "control_8.py", line 3, in <module>
    x = int(input('Enter a digit: '))
ValueError: invalid literal for int() with base 10: '4.5'

F:\PY>py control_8.py
Enter a digit: 9
NINE

F:\PY>py control_8.py
Enter a digit: 00
ZERO

F:\PY>py control_8.py
Enter a digit: 0.0
Traceback (most recent call last):
  File "control_8.py", line 3, in <module>
    x = int(input('Enter a digit: '))
ValueError: invalid literal for int() with base 10: '0.0'

F:\PY>py control_8.py
Enter a digit: 0000000
ZERO

F:\PY>py control_8.py
Enter a digit: -1

F:\PY>
"""