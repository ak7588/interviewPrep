"""

Given an array of integers (which may include repeated integers),
determine if there's a way to split the array into two subsequences A and B such that the sum of the integers in both arrays is the same,
and all of the integers in A are strictly smaller than all of the integers in B.

[1,2,3] & [6]

[1+2] [3+6]

[1+2+3] [6]

1. sort the array
2. split the array into two halves
3. count the sum in both parts
4. if left_sum > right_sum:
4.1. move the smallest element from right_sum to left_sum
4.2. otherwise move from left_sum to right_sum
5. if at some point the sum is equal, check if the elements in the second are greater, if so, return true; else, false
5.1. but if it comes to the point that one of the arrays is empty, return false

[2,1,2,5]

[1,2,2,5]

left = [1,2], sum = 3
right = [2,5], sum = 7
[1,2,2] [5]

[3,6,3,4,4]
[3,3,4,4,6]

left = [3,3], sum = 6
right = [4,4,6], sum = 14
"""

def balancedSplitExists(arr):
  if not arr:
    return False
  arr = arr.sort()
  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid+1:]
  while len(left) != 0 or len(right) != 0:
    if sum(left) == sum(right):
      return checkIfOneElementIsLess(left, right)
    elif sum(right) > sum(left):
      left.append(right[0])
      right.delete(right.index(0))
    elif sum(left) > sum(right):
      return False
      
def checkIfOneElementIsLess(left, right) -> Bool:
  left_ind = 0
  right_ind = 0
  while left_ind < len(left) or right_ind < len(right):
    if right[right_ind] > left[left_ind]:
      left_ind += 1
      right_ind += 1
    else:
      return False
  return True
    
