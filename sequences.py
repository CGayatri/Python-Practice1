# ********************** Sequences in Python - Group of elements/items *********************

#string - group of characters
#str s = 'Welcome s'
s = 'Welcome s'
print('s =', s)
str = "Welcome str"
print("str =", str)

#Output :
#F:\PY>py sequences.py
#s = Welcome s
#str = Welcome str

str1 = """This is a book on Python which 
discusses all the topics of 'Core Python' 
in a valid lucid maner."""
print('str1 =', str1)

str2 = '''This is a book on Python which 
discusses all the topics of 'Core Python' 
in a valid lucid maner.'''
print('str2 =' , str2)

#Output:
'''
str1 = This is a book on Python which
discusses all the topics of 'Core Python'
in a valid lucid maner.
str2 = This is a book on Python which
discusses all the topics of 'Core Python'
in a valid lucid maner.
'''


# slice operator 
s = "Welcome to Core Python"                                #this is the original string
print(s)
#Welcome to Core Python

print('0th character s[0] is,', s[0])                       #0th character s[0] is, W
print('charcters from 3rd to 6th :', s[3:7])                #charcters from 3rd to 6th : come
print('from 11th character onwards till end :', s[11:])     #from 11th character onwards till end : Core Python

#display last character of the string 
print('last char :', s[-1])                                 #last char : n

# repetition operator 
print("print original string twice :", s*2)                 #print original string twice : Welcome to Core PythonWelcome to Core Python


# bytes datatype - group o byte numbers (+ve nos fromo 0 to 255 inclusive)

elements = [10, 20, 0, 40, 15]                              #this is a list of byte numbers
x = bytes(elements)                                         #convert the list into bytes array
print(x[0])                                                 #display 0th element, i.e. 10

# x[0] = 30
#throws error:
#Traceback (most recent call last):
#  File "sequences.py", line 58, in <module>
#    x[0] = 30
#TypeError: 'bytes' object does not support item assignment


print(type(x))
#<class 'bytes'>






