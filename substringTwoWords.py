'''
Write a function that takes in two strings and returns true if the second string is substring of the first, and false otherwise.

Algorithm:
- longest string is a dict
- loop through other string's chars
- check if char is in dict
O(n)

Nope that won't work. Different approach:
- still place everything in the dict
- run a second loop to check if it's inside

'''
def isSubstring(str1, str2):
  charDict = {}
  for char in max(len(str1), len(str2)):
    if char not in charDict:
      charDict[char] = 1
    else:
      charDict[char] += 1
  for char in min(len(str1), len(str2)):
    if char not in charDict:
      return False
  return True

'''
Reflection: not sure how to check for consecutiveness. Will look this up now.
Hint: try to traverse both strings at the same time from left to right
Continued solution:
'''

def isSubstring(str1, str2): 
  if str1 == "" or str2 == "":
    return False
  leftStr1 = 0
  leftStr2 = 0
  for i in range(min(len(str1), len(str2))):
    if str1[leftStr1] != str2[leftStr1]:
      leftStr1 += 1
    else:
      leftStr1 += 1
      leftStr2 += 1
      
'''
Still not the right solution, but on the right path. How about trying recursion? Will continue in a bit.
'''
        
