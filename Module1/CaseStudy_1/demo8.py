# 8.With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],   
# write   a program to make a list whose elements are intersection of the above given lists.


def intersection(l1, l2):
    # way - 1 
    #return list(set(l1) & set(l2))         # [35]
    
    # way - 2 : with built-in function set.intersection()
    #return set(l1).intersection(l2)        # def intersection1(l1, l2):
    
    # way - 3 
    #l3 = [value for value in l1 if value in l2]
    #return l3                              # [35]
    
    # way - 4 : hybrid method ---> efficient way - O(n)
    #temp = set(l1)
    #l3 = [value for value in temp if value in l2]   
    #return l3                               # [35] 
    
    # way - 5 : using filter() and lambda 
    l3 = list(filter(lambda x : x in l1, l2))
    return l3                               # [35]


l1 = [1,3,6,78,35,55]
l2 = [12,24,35,24,88,120,155]
print(intersection(l1, l2))



'''
lst1 = [9, 9, 74, 21, 45, 11, 63] 
lst2 = [4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91] 
print(intersection(lst1, lst2)) 


F:\PY\Module1\CaseStudy_1>py demo8.py
[9, 11]

'''

'''
F:\PY\Module1\CaseStudy_1>py demo8.py
[35]
'''


#print(intersection1(l1, l2))
'''
F:\PY\Module1\CaseStudy_1>py demo8.py
{35}
'''