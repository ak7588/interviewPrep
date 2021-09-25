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
  def helper(root):
    if root is None:
      return None
    if rounded(target) == root.data:
      return root.data
    if target > root.right.data:
      helper(root.right)
    if target < root.left.data:
      helper(root.left)
  return helper(root)
