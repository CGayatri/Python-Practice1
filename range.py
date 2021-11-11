# range datatype - a sequence of numbers
# numbers in range are not modifiable
# used in for loops - for repeating a for loop for a specific numbers of tiimes

# creat a range object with the numbers starting from 0-9
r = range(10)

# display range using for loop
for i in r : print(i)


#Output:
#F:\PY>py range.py
#0
#1
#2
#3
#4
#5
#6
#7
#8
#9


#create a range object including step value --> start, stop, step
r1 = range(30, 39, 2)

for i in r1 : print(i)

#output:
#30
#32
#34
#36
#38

# create a list with a range of numbers from 0 to 9; use list() function
lst = list(range(10))

print(lst)              #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



print(type(r))
#<class 'range'>
print(type(lst))
#<class 'list'>
