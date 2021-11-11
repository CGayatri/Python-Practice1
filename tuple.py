# tuple datatype
tpl = (10, -20, 15.5, 'Vijay', "Mary")

print(tpl[0])   #10

#try modifying, uples are not modifiable
#tpl[1] = -10

#Output : error: 
#Traceback (most recent call last):
#  File "tuple.py", line 7, in <module>
#    tpl[1] = -10
#TypeError: 'tuple' object does not support item assignment


print(type(tpl))
#<class 'tuple'>