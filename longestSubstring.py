"""
Given a string s, find the length of the longest substring without repeating characters.

Edge-cases / Q: empty string, numerical characters inside, all of the chars are the same

Algorithm:
1. Iterate through the str
2. Create an empty str to which I will append if the char isn't already in the new str
3. Count the number of chars in new str and reset if char is repeated
4. Store these reset values and return the max


s = "abcabcbb"
substring = "b"
max = 3
"""

def findLongestSubstring(str):
  if str == "":
    return 0
  substring_len_count = 0
  max_length = 0
  start_index = 0
  chars_dict = {}
  for i, char in enumerate(s):
    if char not in chars_dict or chars_dict[char] < start_index:
      substring_len_count += 1
      chars_dict[char] = i
    else:
      old_index = chars_dict[char]
      chars_dict[char] = i
      max_length = max(max_length, substring_len_count)
      start_index = old_index
      substring_len_count = i - old_index
   return max(substring_len_count, max_length)
  
  
