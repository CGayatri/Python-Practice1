#*********** DATA TYPEs ***************

#None data type

#a=None
#print(a)

x = None 

if x:
    print("True")
else :
    print("False")
    
    
    
    
#Complex data type

#program to add two integers 
i1 = 45
i2 = -85
i3 = i1 + i2
print("Sum of integer numbers = " , i3)

#program to add two float numbers 
f1 = 4.555
f2 = -8.5e4
f3 = f1 + f2
print("Sum of integer numbers = " , f3)

#python program to add two complex numbers
c1 = 2.5+2.5j
c2 = 3.0-0.5J
c3 = c1 + c2
print("Sum of complex numbers = ", c3)




# bool Datatype

a = 10
b = 20
if (a < b): 
    print("if a is less than b display - Hello")  
#display Hello if a is less than b
    

a = 10>5    #here 'a' is treated as a bool type varible 
print(a)    #True

a = 5>10
print(a)    #False


# True = 1 and False = 0
print(True+True)    #2
print(True+False)   #1


# determining data type of a variable -  type() fuction
print(type(c3))     #<class 'complex'>



# character 
ch = 'A'
print(type(ch))
#<class 'str'>

str = "Bharat"
for i in str : print(i)

#B
#h
#a
#r
#a
#t

#print(str[0].isupper)
#<built-in method isupper of str object at 0x000002AD23516EF0>

print(str[0].isupper())
#True

print(str[1].isupper())
#False