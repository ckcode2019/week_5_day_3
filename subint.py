"""
Create a function that takes a number and a list of numbers as a parameter and returns the 
indeces of the numbers of the list which contain the given number
 or returns an empty list (if the number is not part of any of the numbers in the list)

print(find_matching_indexes(1, [1, 11, 34, 52, 61])) should print: [0, 1, 4] 
print(find_matching_indexes(9, [1, 11, 34, 52, 61])) should print: '[]

'"""

def find_matching_indexes(the_number, the_list):
  return_list= []
  for i,j in enumerate(the_list):
    k = str(j)
    for m in k:
      if m == str(the_number):
        return_list.append(i)
        break

  return return_list
       
print(find_matching_indexes(1, [1, 11, 34, 52, 61]))

