# input: an array of integers
# output: an integer, how many da operations are needed to sort this array
#Instructions:
#Given an array of integers, find out the minimum number of Delete-Append operations that are required to make the array sorted. 

#You can solve this problem in a number of ways. 
#Hint 1: Could you somehow find out how many operations are necessary by looking at the already sorted version of the array?
#Hint 2: Alternatively, it is possible to find out the minimum number of required operations without sorting the list?

#Example:
#[1, 5, 2, 4, 3, 6]; Starting array
#[1, 5, 2, 3, 6, 4]; DA 4
#[1, 2, 3, 6, 4, 5]; DA 5
#[1, 2, 3, 4, 5, 6]; DA 6

#Done! Took three operations.
def da_sort(nums):
  in_place_nums = []
  minimum_oop = None
  
  for num in nums:
    while (len(in_place_nums) > 0 and num < in_place_nums[-1]):
      if minimum_oop is None or num < minimum_oop:
        minimum_oop = in_place_nums.pop()
      else:
        in_place_nums.pop()
    in_place_nums.append(num)
    
  while in_place_nums[-1] > minimum_oop:
    in_place_nums.pop()
  
  return len(nums) - len(in_place_nums)
  
print(da_sort([1, 5, 2, 4, 3, 6]))