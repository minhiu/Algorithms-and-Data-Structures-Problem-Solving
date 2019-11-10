#Given an integer n, return the number of trailing zeroes in n!.

def fast_trailing_zero_factorial(n):
  if n < 5:
    return 0;
  
  return int(n / 5) + fast_trailing_zero_factorial(n/5)


#Test
print(fast_trailing_zero_factorial(1))
fast_trailing_zero_factorial(5)
fast_trailing_zero_factorial(9)
fast_trailing_zero_factorial(14)
fast_trailing_zero_factorial(23)