#Given two strings s and t , write a function to determine if t is an anagram of s.
#Input: s = "anagram", t = "nagaram"
#Output: true

#Input: s = "rat", t = "car"
#Output: false

def valid_anagram(s,t):
  if len(s) != len(t):
    return False
    
  if sorted(s) == sorted(t):
    return True
  
  return False

valid_anagram("rat", "car")
valid_anagram("anagram", "nagaram")