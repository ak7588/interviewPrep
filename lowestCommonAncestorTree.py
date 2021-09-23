"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

Edge-cases: is it possible that the tree is empty? Or that the nodes are invalid? Can nodes be repeated?

Algorithm:

0. search for both nodes?
1. iterate, return (node.val, True/False)
2. iterate, return first elem that has [1] = True

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lowestCommonAncestorNode = None
        def preorder_traversal(node):
          if not node:
            return False
          left = preorder_traversal(node.left)
          right = preorder_traversal(node.right)
          mid = node == p or node == q
          if mid + left + right >= 2:
            self.lowestCommonAncestorNode = node
          return mid or right or left
        preorder_traversal(root)
        return lowestCommonAncestorNode
        
          
          
        
        
