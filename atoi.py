#Implement atoi which converts a string to an integer.

#The function first discards as many whitespace characters as 
#necessary until the first non-whitespace character is found. Then, 
#starting from this character, takes an optional initial plus or minus 
#sign followed by as many numerical digits as possible, and interprets 
#them as a numerical value.

#The string can contain additional characters after those that form 
#the integral number, which are ignored and have no effect on the 
#behavior of this function.

#If the first sequence of non-whitespace characters in str is not a 
#valid integral number, or if no such sequence exists because either 
#str is empty or it contains only whitespace characters, no conversion 
#is performed.

#If no valid conversion could be performed, a zero value is returned.

def atoi(a):
  result = ""
  acceptSigns = True
  isValid = False
  
  for character in a:
      if character.isspace() and isValid or character.isspace() and not acceptSigns:
          break
      
      elif character.isspace():
          pass
           
      elif character.isnumeric():
          result += character
          acceptSigns = False
          isValid = True
          
      elif character == '+' and acceptSigns or character == '-' and acceptSigns:
          result += character
          acceptSigns = False

      elif character == '+' or character == '-':
          break 
      
      elif character.isalpha and not isValid:
          return 0
      
      elif character.isalpha:
          break
      
  if result == "" or result == "+" or result == "-":
      return 0
  
  intResult = int(result)
  
  INT_MAX = 2**31 - 1
  INT_MIN = (-2**31)
  
  if intResult > INT_MAX:
      intResult = INT_MAX
  elif intResult < INT_MIN:
      intResult = INT_MIN
      
  return intResult

#Test
print(atoi("-42"))
print(atoi("4193 with words"))
print(atoi("words and 987"))