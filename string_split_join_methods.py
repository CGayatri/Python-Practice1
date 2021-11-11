## Splitting and Joining Strings

# string.split(seperator)       --> returns a List 
# separator.join(tuple/list of string)    --> returns a String

str = 'one, two, three, four'

str1 = str.split(',')

print(str1)

'''
F:\PY>py string_split_join_methods.py
['one', ' two', ' three', ' four']
'''


print()

tpl_str = ('one', 'two', 'three', 'four')

# output string - tpl_str1 
tpl_str1 = "-".join(tpl_str)

print(tpl_str1)
#one-two-three-four


print()

list_str = ['apple', 'guava', 'grapes', 'mango']

# output string - list_str1
list_str1 = ':'.join(list_str)

print(list_str1)
#apple:guava:grapes:mango


'''
F:\PY>py string_split_join_methods.py
['one', ' two', ' three', ' four']

one-two-three-four

apple:guava:grapes:mango

F:\PY>
'''