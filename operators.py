# Operators


###### Arithmetic Operators
x = 1
y = 2
z = 3
a, b, c = 2, 2, 3

d = (x+y)*z**a//b+c
print('d =', d)         #d = 16


####### Unary Operator

num = -10 
num = -num
print('num =', num)     #num = 10



###### Relational Operators

a=1; b=2;
if (a>b):
    print("Yes")
else:
    print("No")
#No

x=15
print(10<x<20)          #True
print(10>=x<20)         #False
print(10<x>20)          #False

print(1<2<3<4)          #True
print(1<2>3<4)          #False
print(4>2>=2>1)         #True


####### Logical Operators ------------------- Yet to study
####### Bitwise Operators ------------------- Yet to study


######### Boolean Operators : and, or, not

print()
print("####### Boolean Operators #######")

a = True
b = False 
print(a and a)      #True
print(b and b)      #False
print(a and b)      #False

print(a or a)       #True
print(b or b)       #False 
print(a or b)       #True

print(not a)        #False
print(not b)        #True


######### Membership Operators :  in, not in
print()
print("####### Membership Operators ######")
#names : ['Rani', 'Yamini', 'Sushmita', 'Veena']

names = ["Rani", "Yamini", "Sushmita", "Veena"]
print("names :", names)

for name in names:
    print(name)

#Rani
#Yamini
#Sushmita
#Veena

print()
print("Adding a bew name to existing names :: ")

newStudent = "Gayatri"
if(newStudent not in names):
    names.append(newStudent)
for name in names:
    print(name)
    
#AttributeError: 'list' object has no attribute 'add'

'''
#Output:
Adding a bew name to existing names ::
Rani
Yamini
Sushmita
Veena
Gayatri
'''

print("check for not in operator :")
print(newStudent not in names)           #False
print(newStudent in names)               #True
print()



###### ex 2

postal = {'Delhi':110001, 
'Chennai':600001,
'Kolkata':700001,
'Bengaluru':560001}

for city in postal:
    print(city, postal[city])

#Output : 
'''
Delhi 110001
Chennai 600001
Kolkata 700001
Bengaluru 560001
'''



######## Identity Operators : is, is not
a = 25
b = 25
if (a is b):
    print("a and b have same identity")
else :
    print("a and b do not have same identity")
    
#a and b have same identity

####### ex -2 
print()
one = [1, 2, 3, 4]
two = [1, 2, 3, 4]
if (one is two):
    print("one and two are same")
else :
    print("one and two are not same")
    
#one and two are not same
print("id of one :", id(one))       #id of one : 2036943960640
print("id of two :", id(two))       #id of two : 2036945548352




#### ex - 3 
print()
list1 = [1, 2, 3, 4, 5]
list1 = [1, 2, 3, 4, 5]
if (list1 is list1):
    print("both lists are same")
else :
    print("both lists are not same")
    
#both lists are same

#### ex - 4 
print()

list1 = [1, 2, 3, 4, 5]
print("list1 with 1,2,3,4,5 id : ", id(list1))      #list1 with 1,2,3,4,5 id :  2494817977664
list1 = [1, 2, 3, 4]
print("list1 with 1,2,3,4 id :" , id(list1))        #list1 with 1,2,3,4 id : 2494817978560
if (list1 is list1):
    print("both lists are same")
else :
    print("both lists are not same")
    
#both lists are same