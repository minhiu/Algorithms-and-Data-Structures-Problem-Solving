#You are given a string. The only operation allowed is to insert characters in the beginning of the string. 
#Return the number of characters that are needed to be inserted to make the string a palindrome string

def minimumCharacters(inputStr):
  result = 0
  adjustedIndex = 0
  while (inputStr != inputStr[::-1]):
    index = len(inputStr) - 1 - adjustedIndex
    inputStr = inputStr[:result] + inputStr[index] + inputStr[result:]
    adjustedIndex += 1
    result += 1
    
  return result

print(minimumCharacters("ABC"))