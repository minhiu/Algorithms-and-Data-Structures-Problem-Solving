def find_pivot_index(input_list):
  # List is sorted, but then rotated.
  # Find the minimum element in less than linear time
  # return it's index

  start = 0
  end = len(input_list)
  min_index = 0
  
  while start < end:
    pivot = end + (start - end) // 2
    
    if input_list[pivot] < input_list[min_index]:
      min_index = pivot
      end = pivot
    
    else:
      start = pivot + 1
  
  return min_index


print(find_pivot_index([3,4,5,6,7,0,1,2]))