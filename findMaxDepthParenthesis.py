"""
Given a string of type “(({X}({Y})))(Z)”, determine the max depth of nested parentheses in the string. Answer is in this case 4.
Parentheses without variables in them do not count.
"""

def findMaxDepth(str):
  count = 0
  res = 0
  for i in range (len(str)):
    if str[i] in "({":
      count += 1
    elif str[i] in ")}":
      if i > 0 and str[i-1] not in ")}":
        res = max(count, res)
      count -= 1
  return res
        
