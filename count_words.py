#Given a long text string, count the number of occurrences of each word. Ignore case. Assume the boundary of a word is whitespace - a " ", or a line break denoted by "\n". Ignore all punctuation, such as . , ~ ? !. Assume hyphens are part of a word - "two-year-old" and "two year old" are one word, and three different words, respectively. 

#Return the word counts as a string formatted with line breaks, in no particular order.

def count_words(text):
  a_dict = {}
  
  splittedText = text.split()
  
  for string in splittedText:
    string = string.lower().replace(',', '').replace(' ', '')
    if string in a_dict:
      a_dict[string] += 1
    else:
      a_dict[string] = 1
  
  
  result = ""
  for key, value in a_dict.items():
    result += key + ' ' + str(value) + '\n'
  
  return result

print(count_words("I do not like green eggs and ham," +
"I do not like them, Sam-I-Am"))

