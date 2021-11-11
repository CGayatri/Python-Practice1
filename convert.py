# *********** TYPE CONVERSION / COERCION ***************

# To convert binary, octal, and hexadecimal numbers into decimal integers using type conversion

# program to convert into decimal number system  - v1.0
n1 = 0o17       #Octal
n2 = 0B1110010  #Binary
n3 = 0X1c2      #Hexadecimal

print("n1 = ", n1)
print("n2 = ", n2)
print("n3 = ", n3)

n = int(n1)
print('Octal 17 = ', n)

n = int(n2)
print('Binary 1110010 = ', n)

n = int(n3)
print('Hexadecimal 1c2 = ', n)

#Output

#F:\PY>py convert.py
#n1 =  15
#n2 =  114
#n3 =  450
#Octal 17 =  15
#Binary 1110010 =  114
#Hexadecimal 1c2 =  450

str = "1c2"             #string str contains a hexadecimal number
print("str = ", str)

n = int(str, 16)        # hence base is 16, Convert str into int 
print(n)                #this would display 450

#n = int(str, 8)        # hence base is 16, Convert str into int 
#print(n)               #this above line-39 would throw an error : 
                            #Traceback (most recent call last):
                            #  File "convert.py", line 39, in <module>
                            #    n = int(str, 8)    # hence base is 16, Convert str into int
                            #ValueError: invalid literal for int() with base 8: '1c2'




# rewrite above program v1.0 using int() function to convert numbers from different number systems into decimal number system.
# program to convert into decimal number system - v2.0

s1 = "17"
s2 = "1110010"
s3  = "1c2"

print ("s1 = ", s1)
print ("s2 = ", s2)
print ("s3 = ", s3)

n = int(s1, 8)
print('Octal 17 = ', n)

n = int(s2, 2)
print('Binary 1110010 = ', n)

n = int(s3, 16)
print('Hexadecimal 17 = ', n)

#Output
#s1 =  17
#s2 =  1110010
#s3 =  1c2
#Octal 17 =  15
#Binary 1110010 =  114
#Hexadecimal 17 =  450


a = 10
b = bin(a)
#print('binary of a = ", b)     #Error ====>   File "convert.py", line 81    print('binary of a = ", b)  SyntaxError: EOL while scanning string literal
print('binary of a =' , b)      #binary of a = 0b1010

o = oct(a)
print('octal of a =', o)        #octal of a = 0o12

h = hex(a)
print('hex of a =', h)          #hex of a = 0xa


print(type(h))                  #<class 'str'>
















