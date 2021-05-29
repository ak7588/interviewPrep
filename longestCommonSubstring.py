'''
Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.
'''

'''
1. Create a dict for all chars in string 1 { char: count }
2. Create a dict for all chars in string 2 { char: count }
3. Iterate through longest string and see if any of the keys from dict 1 are in the dict 2
4. If so, count how many
5. Return the count
'''

def getLongestCommonSubstring(str1, str2):
  
  if len(str1) == 0 or len(str2) == 0:
    return 0
  
  dictStr1 = {}
  dictStr2 = {}
  longestCommonCount = 0
  
  for char in str1:
    if char not in dictStr1:
      dictStr1[char] = 1
    else:
      dictStr1[char] += 1
  
  for char in str2:
    if char not in dictStr2:
      dictStr2[char] = 1
    else:
      dictStr2[char] += 1
  
  if len(str1) > len(str2):
    for char in str2:
      if char in dictStr1:
        longestCommonCount += 1
  else:
    for char in str1:
      if char in dictStr2:
        longestCommonCount += 1
        
  return longestCommonCount

# Update: solution incorrect because it does not use dynamic programming
    
