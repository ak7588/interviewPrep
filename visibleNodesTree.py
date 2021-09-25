"""
There is a binary tree with N nodes. You are viewing the tree from its left side and can see only the leftmost nodes at each level. Return the number of visible nodes.
Note: You can see only the leftmost nodes, but that doesn't mean they have to be left nodes. The leftmost node at a level could be a right node.


"""

def visible_nodes(root) -> Int:
  if not root:
    return None
  count = 0
  maxLevel = 1
  def helper(level, root):
    nonlocal maxLevel
    if root:
      if maxLevel == level:
        count += 1
        maxLevel += 1
      helper(level + 1, root.right)
      helper(level + 1, root.left)             
  helper(1, root)
  return count
