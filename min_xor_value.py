#Given a list of unsigned integers, find the pair of integers in the #array which have the minimum XOR value. Return the minimum XOR value.

def min_xor_value(num):
  min_value = num[0] ^ num[1]
  
  for i in range(0, len(num) - 2):
    if (num[i+1] ^ num[i+2]) < min_value:
      min_value = (num[i+1] ^ num[i+2])
  
  return min_value

 print(min_xor_value([0,2,4,6]))