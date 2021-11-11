## String Testing Methods - to test the nature of characters in a string --> retrn bolean True/False

str = 'Delhi999'

print('Delhi999.isalnum() :', str.isalnum())
#str.isalnum() : True
#Delhi999.isalnum() : True

print('Delhi999.isalpha() :', str.isalpha())
#Delhi999.isalpha() : False

str = 'Delhi'
print('Delhi.isalpha() :', str.isalpha())
#Delhi.isalpha() : True

num = '123654'
print('123654.isdigit() :', num.isdigit())
#123654.isdigit() : True

low = 'abcde'
print('abcde.islower() :', low.islower())
#abcde.islower() : True

up = 'A'
print('A.isupper() :', up.isupper())
#A.isupper() : True

title = 'Python Is a Future'
print('title.istitle() :', title.istitle())
#title.istitle() : False

title = title.title()       # if it's not title, make it title and then test 
print('title.istitle() :', title.istitle())
#title.istitle() : True

strspace = "    "
print('    .isspace() :', strspace.isspace())
#    .isspace() : True
