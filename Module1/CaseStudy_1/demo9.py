# 9. With a given list [12,24,35,24,88,120,155,88,120,155], 
# write a program to print this list after removing all duplicate values with original order reserved.

original_list = [12,24,35,24,88,120,155,88,120,155]

filtered_list = []

# Naive method 
for i in original_list:
    if i not in filtered_list:
        filtered_list.append(i)
  
print(filtered_list)


'''
F:\PY\Module1\CaseStudy_1>py demo9.py
[12, 24, 35, 88, 120, 155]

'''

# way - 2 : using list comprehension 
'''
----- NOT WORKING 
filtered_list = [value for value in original_list if value not in filtered_list]
print(filtered_list)
'''