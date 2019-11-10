#Input
#The first line of input contains a single decimal integer P, (1≤P≤1000), which is the number of data sets that follow. Each data set should be processed identically and independently.

#Each data set consists of a single line of input. 
#It contains the data set number, K, 
#followed by the base, b (3≤b≤16) as a decimal integer, 
#followed by the positive integer, n (as a decimal integer) for which the Sum Squared Digits function is to be computed with respect to the base b. n will fit in a 32 bit unsigned integer. The data set number K starts at 1 and is incremented by 1 for each data set.


#Output

#For each data set there is a single line of output.
#The single line of output consists of the data set number, K, 
#followed by a single space followed by the value of SSD(b,n) as a decimal integer.

#Sample Input 1

#3
#1 10 1234
#2 3 98765
#3 16 987654321

#Sample Output 1
#1 30
#2 19
#3 696

def sum_of_squares(k, b, n):
 result = 0
 while n != 0:
   remainder = n % b
   n = int(n / b)
   result += remainder ** 2
 print(k, result)

# read first line
number_of_lines = int(input())

# read all remaining lines
for i in range(number_of_lines):
 line = input()
 args = line.split();
 k = int(args[0]);
 b = int(args[1]);
 n = int(args[2]);

 sum_of_squares(k, b, n)