"""

Given an array of strings (all lowercase letters), the task is to group them in such a way that all strings in a group are shifted versions of each other.

Two string S and T are called shifted if:

- S.length = T.length 
- S[i] = T[i] + K for 1 <= i <= S.length  for a constant integer K

1. Can an array be empty and include non-strings?
2. Are there any alpha-numeric or non-alpha-numeric chars?
3. In what way should the grouping take place?
4. Same string multiple times?

Algorithm:
1. Sort the array by the length
1.2. Create a dict with length as a key and array of strings of the same length as a value
2. Take all of the elements of the same length and compare their alpha/ASCII value difference
2.1. If the same difference, then they're shifted -> group together

Comparing:
1. ord(char) -> ASCII
"""

def getShiftedStringGroups(arr):
  
  def shiftedString(str):
    shifted = ""
    for i in range(1, len(str)):
      diff = (ord(str[i]) - ord(str[i - 1]))
      if diff < 0:
        diff += 26
      shift += chr(diff + ord('a'))
    return shift
        
  grouped_by_length = {}
  for str in arr:
    shifted_val_str = shiftedString(str)
    if shifted_val_str not in grouped_by_length:
      grouped_by_length[shifted_val_str] = [str]
    else:
      grouped_by_length[shifted_val_str].append(str)
