"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

Algorithm:
1. find max and min and determine if the target is in that range
1.2. if it is, just search for lower and higher estimation

"""

def findClosestValueBST(root, target):
  def findMaxAndMin(root):
    if root is None:
      return
    stack = []
    stack.append(root)
    max_elem = root.data
    min_elem = root.data
    while len(stack) > 0:
      curr = stack.pop()
      if curr.data > max_data:
        max_elem = curr.data
      if curr.data < min_elem:
        min_elem = curr.data
      if curr.left is not None:
        stack.append(curr.left)
      if curr.right is not None:
        stack.append(curr.right)
    return max_elem, min_elem
  max, min = findMaxAndMin(root)
  if max > target and min < target:
    # search
  
    
