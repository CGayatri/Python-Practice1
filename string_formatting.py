## Formatting the Strings- format() method

# 'format string with replacement fields'.format(values)

id = 10
name = 'Omkar'
sal = 70000.75

str = '{},{},{}'.format(id, name, sal)

print(str)
#10,Omkar,70000.75

str = '{}-{}-{}'.format(id, name, sal)

print(str)
#10-Omkar-70000.75
'''
Traceback (most recent call last):
  File "string_formatting.py", line 14, in <module>
    str = '{}-{}-{}'.format(id, anme, sal)
NameError: name 'anme' is not defined
'''

print()

str1 = 'Id= {} \nName={} \nSalary= {}'.format(id, name, sal)
print(str1)
'''
Id= 10
Name=Omkar
Salary= 70000.75
'''

print()
str2 = 'Id= {0} \nName={1} \nSalary= {2}'.format(id, name, sal)
print(str2)
'''
Id= 10
Name=Omkar
Salary= 70000.75
'''

print()
str3 = 'Id= {2} \nName={0} \nSalary= {1}'.format(id, name, sal)
print(str3)
'''
Id= 70000.75
Name=10
Salary= Omkar
'''

print()
str4 = 'Id= {2} \tName={0} \tSalary= {1}'.format(id, name, sal)
print(str4)
#Id= 70000.75    Name=10         Salary= Omkar


print()
str5 = 'Id= {one}, Name= {two}, Salary= {three}'.format(one=id, two=name, three=sal)
print(str5)
#Id= 10, Name= Omkar, Salary= 70000.75


print()
str6 = 'Id = {:d}, Name = {:s}, Salary = {:10.2f}'.format(id, name, sal)
print(str6)
#Id = 10, Name = Omkar, Salary =   70000.75

#=================================================================================================

print()
num = 5000
strnum = '{:*>15d}'.format(num)
print(strnum)
#***********5000

strnum1 = '{:*^15d}'.format(num)
print(strnum1)
#*****5000******

strnum2 = '{:*<15d}'.format(num)
print(strnum2)
#5000***********

#=================================================================================================

# display a value in Hexadecimal and Binary number 
n1 = 1000

print('Hexadecimal = {:@>15x}'.format(n1))
#Hexadecimal = @@@@@@@@@@@@3e8

print('Binary = {:@>15b}'.format(n1))
#Binary = @@@@@1111101000

print('Hexadecimal = {:@>15x}\nBinary = {:@>15b}'.format(n1, n1))
'''
Hexadecimal = @@@@@@@@@@@@3e8
Binary = @@@@@1111101000
'''

# display these numbers by adding the appropriate prefixes 0x and 0b, we can add a hash(#) n replacement fields

n1 = 1000
print('Hexadecimal = {:.>#15x} \nBinary = {:.<#15b}'.format(n1, n1))
'''
Hexadecimal = ..........0x3e8
Binary = 0b1111101000...
'''















