"""
Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, each copy is considered to be different;
that is, two pairs are considered different if one pair includes at least one array index which the other doesn't, even if they include the same values.

Edge-cases: empty array, no sum, are all integers?
Algorithm:
1. iterate over list and create a dictionary
2. dict[i] = k - i
3. if there's an element that is diff and is in the dict, increment the number of ways

"""

def numberOfWays(arr, k):
  diff_dict = {}
  count = 0
  for i in range(len(arr)):
    if (k - arr[i]) in diff_dict:
      count += 1
    if arr[i] not in diff_dict:
      diff_dict[arr[i]] = k - arr[i]
  return count
      
