## Counting Substrings in a String - count() method ; returns int value i.e. how many tims substring is found in main string 

# stringname.count(substring)
# stringname.count(substring, startPOs, endPos)

str = 'New Delhi'
n = str.count('Delhi')

print(n)
#1

n = str.count('e', 0, -1)
print(n)
#2

n = str.count('e', 0 , 3)
print(n)
#1

n = str.count('e', 0, len(str))
print(n)
#2