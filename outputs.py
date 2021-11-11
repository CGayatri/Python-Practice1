############## Output Statements ###############

## print() stmt
print()

'''
F:\PY>py outputs.py


F:\PY>
'''



## print("string") stmt
print("Hello Double quotes")
'''
Hello Double quotes

'''

print('Hello Single quotes')
'''
Hello Single quotes

'''

# use of escape character - \n, \\, \t, \', \", \\n
print("This is the \nfirst line")
'''
This is the
first line
'''

print("This is the \tfirst line")
#This is the     first line

print('this is the \\nfirst line')
#this is the \nfirst line

print(3*'Hai')
#HaiHaiHai

# + operator on number - arithmetic 
print(4+5)
#9

# + operator on strings - concatenation
print("City name="+"Pune")
#City name=Pune

# using comma - a default space get added in between strings , cuz comma assumes values are different and hence space should be added 
print("City name=","Pune")
#City name= Pune



## print(variale list) stmt
a, b = 2, 4
print(a)
#2

print(a, b)
#2 4

## 'sep' attribute - separator

print(a, b, sep=",")
#2,4

print(a, b, sep=':')
#2:4

print(a, b, sep='----')
#2----4

# several print() functions display outputs on separate new lines
print("Hello")
print("Dear")
print('How are u?')
'''
Hello
Dear
How are u?

'''

## 'end' attribute 
print("Hello", end='')
print("Dear", end='')
print('How are u?', end='')
#HelloDearHow are u?

print('\n')

print("Hello", end='\t')
print("Dear", end='\t')
print('How are u?', end='\t')
#Hello   Dear    How are u?

print()




### print(object) stmt

lst = [10, 'A', 'Hai']
print(lst)
#[10, 'A', 'Hai']

d = {'Idli': 30.00, 'Roti':45.00, 'Pulao':55.50}
print(d)
#{'Idli': 30.0, 'Roti': 45.0, 'Pulao': 55.5}

print()


### print("string", variable list) stmt
a = 2 
print(a, "is even number")
#2 is even number

print('You typed ', a, 'as input')
#You typed  2 as input


### print(formatted string) stmt
# %i, %d - integers; %f - floating point numbers; %s - string ; %c - a character 

x = 10 
print('value = %i' %x)
#value = 10

x, y = 10, 15
print('x= %i y=%d' %(x,y))
#x= 10 y=15


name = 'Linda'
print('Hai %s' %name)
#Hai Linda

print('Hai (%20s)' % name)
#Hai (               Linda)

print('Hai (%-20s)' %name)
#Hai (Linda               )

print('Hai %20s' % name)
#Hai                Linda



name = 'Linda'
print('Hai %c, %c' % (name[0], name[1]))
#Hai L, i

print('Hai %s' % name[0:2])
#Hai Li


num = 123.456789
print('The  value is: %f' %num)
#The  value is: 123.456789

print('The value is: %8.2f' %num)
#The value is:   123.46


###  print('formatted string with replacement fields'.format(values))

n1, n2, n3 = 1, 2, 3
print('number1 = {0}'.format(n1))
#number1 = 1


print('number1={0}, number2={1}, number3={2}'.format(n1, n2, n3))
#number1=1, number2=2, number3=3

print('number1={1}, number2={0}, number3={2}'.format(n1, n2, n3))
#number1=2, number2=1, number3=3


### names in replacement fields 
print('number1={two}, number2={one}, number3={three}'.format(one=n1, two=2, three=3))
#number1=2, number2=1, number3=3

### w/o names/indexes
print('number1={}, number2={}, number3={}'.format(n1, n2, n3))
#number1=1, number2=2, number3=3


name, salary = 'Ravi', 12500.75
print('Hello {0}, your salary is {1}'.format(name, salary))
#Hello Ravi, your salary is 12500.75

print('Hello {n}, your salary is {s}'.format(n=name, s=salary))
#Hello Ravi, your salary is 12500.75

print('Hello {:s}, your salary is {:.2f}'.format(name, salary))
#Hello Ravi, your salary is 12500.75

print('Hello {:s}, your salary is {:.1f}'.format(name, salary))
#Hello Ravi, your salary is 12500.8

print('Hello %s, your salary is %.2f' %(name, salary))
#Hello Ravi, your salary is 12500.75



