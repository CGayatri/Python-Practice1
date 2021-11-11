#list1 = ['C++', 'Java', 'Python']
#list1.append('C#')
#print ("updated list : ", list1)

###### List operations

###### adding elements to list
print("###### adding elements to list #########")

langs = ['Java']
langs.append('Python')
langs.append("Perl")
print (langs)               #['Java', 'Python', 'Perl']
print()

langs.insert(0, "PHP")
langs.insert(2, "Lua")
print(langs)                #['PHP', 'Java', 'Lua', 'Python', 'Perl']
print()

langs.extend(("JavaScript", "ActionScript"))
print(langs)                #['PHP', 'Java', 'Lua', 'Python', 'Perl', 'JavaScript', 'ActionScript']
print() 

#Output:
"""
F:\PY>py list1.py
###### adding elements to list #########
['Java', 'Python', 'Perl']

['PHP', 'Java', 'Lua', 'Python', 'Perl']

['PHP', 'Java', 'Lua', 'Python', 'Perl', 'JavaScript', 'ActionScript']
"""
