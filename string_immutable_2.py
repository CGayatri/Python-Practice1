## strings are immutable 

s1 = 'one'
s2 = 'two'

print('Before modify s2 = :: ', s2)

print('id of s1 =', id(s1))
print('id of s2 =', id(s2))

s2 = s1

print(s2)
#one

print(s1)
#one

print()

print('After modification s2 = :: ', s2)
print('Id of s1 : ', id(s1))
print('Id of s2 : ', id(s2))

"""
F:\PY>python string_immutable_2.py
Before modify s2 = ::  two
id of s1 = 2418365324592
id of s2 = 2418365324656
one
one

After modification s2 = ::  one
Id of s1 :  2418365324592
Id of s2 :  2418365324592
"""

"""
F:\PY>python string_immutable_2.py
Before modify ::
id of s1 = 1876755439024
id of s2 = 1876755439088
one
one

Id of s1 :  1876755439024
Id of s2 :  1876755439024
"""

"""
F:\PY>python string_immutable_2.py
Before modify ::
id of s1 = 2287984663920
id of s2 = 2287984663984
one
one

After modification ::
Id of s1 :  2287984663920
Id of s2 :  2287984663920
"""