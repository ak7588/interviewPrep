'''
Write a program to reverse an array or string.
'''

# Space complexity: O(1)
# Time complexity: O(n/2) = O(n)

def reverseArray(lst):
  # edge case 1
  if len(lst) == 0 or len(lst) == 1:
    return lst
  # str is immutable, so edge case 2
  if isinstance(lst, str):
    isStr = true
    lst = list(lst)
  # two pointers to mutate lst in-place
  high_index = 0
  low_index = len(lst) - 1
  while high_index < low_index:
    lst[high_index], lst[low_index] = lst[low_index], lst[high_index]
    high_index += 1
    low_index -= 1
  # back to str if input was a str
  if isStr:
    lst = str(lst)
  return lst
