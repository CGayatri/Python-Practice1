# 11. By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

lst = [12,24,35,70,88,120,155]

newlst = [x for (i,x) in enumerate(lst) if i not in (0,4,5)]

print(newlst)


'''
F:\PY\Module1\CaseStudy_1>py demo11.py
[24, 35, 70, 155]

F:\PY\Module1\CaseStudy_1>
'''