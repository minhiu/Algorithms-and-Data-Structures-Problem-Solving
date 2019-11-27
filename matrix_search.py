#Write an efficient algorithm that searches for a value in an m x n matrix.
#This matrix has the following properties:
#Integers in each row are sorted from left to right.
#The first integer of each row is greater than or equal to the last integer of the previous row.

def matrix_search(matrix, target):
  i = 0
  while (i < len(matrix) - 1):
    if target >= matrix[i+1][0]:
      i += 1
    else:
      break
      
  s = 0
  e = len(matrix[i])
  
  while s < e:
    p = (s + e) // 2
    
    if matrix[i][p] < target:
      s = p + 1
    elif matrix[i][p] > target:
      e = p 
    else:
      return 1
      
  return 0

print(matrix_search([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3))