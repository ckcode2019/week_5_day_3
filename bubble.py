"""
Create a function that takes a list of numbers as parameter and returns a list where the elements 
are sorted in ascending numerical order When you are done, add a second boolean parameter 
to the function If it is true sort the list descending, otherwise ascending

def bubble(arr): pass

def advanced_bubble(arr, is_descending): pass

Example: print(bubble([43, 12, 24, 9, 5])) should print [5, 9, 12, 24, 34] 
print(advanced_bubble([43, 12, 24, 9, 5], True)) should print [34, 24, 9, 5]
"""

# Sort---------------------------------------------------------------------------
def bubble(the_list):
    for x in range(len(the_list)-1, 0, -1 ):
        for j in range(x):
            if the_list[j]>the_list[j+1]:
                the_list[j],the_list[j+1] = the_list[j+1],the_list[j] 
                 
    return the_list


print(bubble([43, 12, 24, 9, 5]))


# r_Sort---------------------------------------------------------------------------

def bubble(the_list, is_descending=False):
    for x in range(0, len(the_list)-1, -1 ):
        for j in range(x):
            if is_descending:
                if the_list[j] < the_list[j+1]:
                    the_list[j], the_list[j+1] = the_list[j+1], the_list[j] 
            else:
                if the_list[j]  > the_list[j+1]:
                    the_list[j], the_list[j+1] = the_list[j+1], the_list[j]

    return the_list


print(bubble([43, 12, 24, 9, 5]),True)