## program - 10: to convert numbers from other systems into decimal number systems 

# input from other number systems 
str = input('Enter hexadecima number: ')        #accept input as a string 
n = int(str, 16)        #inform the number is base 16 
print('Hexadecimal to Decimal= ', n)

str = input('Enter octal number: ')
n = int(str, 8)
print('Octal to Decimal= ',n)

str = input('Enter binary number : ')
n = int(str, 2)
print('Binary to Decimal= ', n) 



'''
F:\PY>py input10.py
Enter hexadecima number: a
Hexadecimal to Decimal=  10
Enter octal number: 10
Octal to Decimal=  8
Enter binary number : 1101
Binary to Decimal=  13
'''