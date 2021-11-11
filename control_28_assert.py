## program 28 - to assert that the user enters a number greater tha zero.

num = int(input('Enter a number greater than 0: '))

assert num>0, "Wrong input entered, it should be greater than 0"

print('U entered: ', num)

"""
F:\PY>py control_28_assert.py
Enter a number greater than 0: 5
U entered:  5

F:\PY>py control_28_assert.py
Enter a number greater than 0: -5
Traceback (most recent call last):
  File "control_28_assert.py", line 5, in <module>
    assert num>0, "Wrong input entered, it should be greater than 0"
AssertionError: Wrong input entered, it should be greater than 0

F:\PY>
"""






#assert (num>0, "Wrong input entered, it should be greater than 0")
'''
F:\PY>py control_28_assert.py
control_28_assert.py:5: SyntaxWarning: assertion is always true, perhaps remove parentheses?
  assert (num>0, "Wrong input entered, it should be greater than 0")
Enter a number greater than 0: 5
U entered:  5

F:\PY>py control_28_assert.py
control_28_assert.py:5: SyntaxWarning: assertion is always true, perhaps remove parentheses?
  assert (num>0, "Wrong input entered, it should be greater than 0")
Enter a number greater than 0: -5
U entered:  -5

F:\PY>
'''