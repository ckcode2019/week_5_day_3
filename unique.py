"""
Create a function that takes a list of numbers as a parameter and returns a list of numbers 
where every number is unique (occurs only once)

def unique(arr): pass


print(find_unique_items([1, 11, 34, 11, 52, 61, 1, 34])) should print: [1, 11, 34, 52, 61]

"""

def find_unique_items(the_list):
    p = []
    for i in the_list:
        if i in the_list and i != "x":
            p.append(i)
            for k, l in enumerate(the_list):
                if l == i:
                    the_list[k] = "x"
    return p

    

print(find_unique_items([1, 11, 34, 11, 52, 61, 1, 34]))


