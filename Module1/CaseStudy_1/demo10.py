# 10. By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

lst = [12,24,35,24,88,120,155]

newlst = [x for x in lst if x != 24]

print(newlst)

'''
F:\PY\Module1\CaseStudy_1>py demo10.py
[12, 35, 88, 120, 155]

F:\PY\Module1\CaseStudy_1>
'''