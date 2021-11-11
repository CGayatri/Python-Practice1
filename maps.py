# mapping types

# create an empty dictonary
d = {}
print(d)
#{}

d[10] = "Kamal"
d[11] = "Pranav"
print(d)
#{10: 'Kamal', 11: 'Pranav'}


# create a dictionary by typing the roll numbers and names of students 
# rolle no - keys; names - values
d = {10:'Kamal' ,
11:'Pranav',
12:'Hasini',
13:'Anup',
14:'John'}

print(d)
#{10: 'Kamal', 11: 'Pranav', 12: 'Hasini', 13: 'Anup', 14: 'John'}

# retrieve particular value
print(d[12])
#Hasini

# get all keys 
print(d.keys())
#dict_keys([10, 11, 12, 13, 14])


# get all values 
print(d.values())
#dict_values(['Kamal', 'Pranav', 'Hasini', 'Anup', 'John'])

# update d
d[10] = "Orange"
print(d)
#{10: 'Orange', 11: 'Pranav', 12: 'Hasini', 13: 'Anup', 14: 'John'}


# delete a pair for key 11
del d[11]
print(d)
#{10: 'Orange', 12: 'Hasini', 13: 'Anup', 14: 'John'}




print(type(d))
#<class 'dict'>

