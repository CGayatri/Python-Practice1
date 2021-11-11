## program - 16 : to accept a tuple and dsplay it 

# accepting a tuple from keyboard 
tpl = eval(input("Enter a tuple: "))
print("Tuple= ",tpl)

"""
F:\PY>py input16.py
Enter a tuple: 10, 20, 30
Tuple=  (10, 20, 30)

F:\PY>py input16.py
Enter a tuple: 10 20 30
Traceback (most recent call last):
  File "input16.py", line 4, in <module>
    tpl = eval(input("Enter a tuple: "))
  File "<string>", line 1
    10 20 30
       ^
SyntaxError: invalid syntax

F:\PY>py input16.py
Enter a tuple: ("Om", 250, 30.9)
Tuple=  ('Om', 250, 30.9)
"""