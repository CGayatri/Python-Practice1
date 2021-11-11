# sets datatypes - unordered collection of elements ; duplicates are not allowed

# set datatype

s = {10, 20, 30, 20, 50}
print(s)            
#{10, 20, 50, 30}


#create a set using set() function
ch = set("Hello")
print(ch)
#{'o', 'l', 'H', 'e'}

#convert a list into a set
lst = [1, 2, 5, 4, 3, 7, 3]
s = set(lst)
print(s)            
#{1, 2, 3, 4, 5, 7}

#print(s[0])
#Traceback (most recent call last):
#  File "sets.py", line 21, in <module>
#    print(s[0])
#TypeError: 'set' object is not subscriptable


# update() method - used to add elements to a set
s.update([50, 60])
print(s)
#{1, 2, 3, 4, 5, 7, 50, 60}

# remove() method - used to remove any particular element from a set 
s.remove(50)
print(s)
#{1, 2, 3, 4, 5, 7, 60}

## frozenset datatype - unmodifiable set 
# can be created using frozenset() function 

s = {50, 60, 70, 80, 90}
print(s)
#{70, 80, 50, 90, 60}

fs = frozenset(s)
print(fs)
#frozenset({80, 50, 70, 90, 60})

fs = frozenset("abcdefg")
print(fs)
#frozenset({'g', 'b', 'e', 'd', 'c', 'a', 'f'})



print(type(s))
#<class 'set'>
print(type(fs))
#<class 'frozenset'>

