# implement a fn that will flatten and sort an array of integers in ascending order
# make sure it adheres to a functional programming paradigm

def flatten_and_sort(array):
  arr = []
  for item in array:
    for i in item:
      arr.append(i)
  return sorted(arr)

print(flatten_and_sort([ [4], [3], [2], [5], [1] ]))

# breaking down what flatten and sorts does because it was a bit complicated for me
# takes the nested arrays and flatten them on the same level so they are no longer nested 
def flatten(array):
  arr = []
  for item in array:
    for i in item:
      arr.append(i)
  return arr

# takes the flatten arrays and sort them into numerical order
def sort_array(array):
  return sorted(array)

test_arr = [[4], [3], [2], [5], [1]]
print(test_arr)

flattend_array = flatten(test_arr)
print(flattend_array)

sorted_array = sort_array(flattend_array)
print(sorted_array)

# Functional Prompt
# 1. How does this solution ensure data immutability?
  # Data that are already inserted cannot be removed (or should not be removed), and modified. Data can only be added.

# 2. Is this solution a pure function? Why or why not?
  # Yes, whenever you call the function, it will give you the same result.

# 3. Is this solution a higher order function? Why or why not?
  # No, you are only returning a sorted array. You are not asking for it to search and return certain things such as multiple of 2 in the array.


# 4. Would it have been easier to solve this problem using a different programming style?
  # No, since you are not using a large amount of data or variables, for it to give the same results with similarities. It should be kept simple.

# 5. Why in particular is functional programming a helpful paradigm when solving this problem?
  # These particular functional programming is helpful because you are forced to break your problems into smaller solutions, which may make it less complicated 