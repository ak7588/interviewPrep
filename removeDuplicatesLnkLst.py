'''
Given a singly linked list consisting of N nodes. The task is to remove duplicates (nodes with duplicate values) from the given list (if exists).
'''
'''
Questions & edge cases:
1. Not empty
2. Does it matter if the stored values are strings, chars, integers / etc?

Brute-force:
- Maintaing a data structure to store unique values (space O(n) - dictionary)
- Iterate through the lnk lst and see if the node is in the data structure (O(n) + O(1))
- If it is, remove that node (O(1))
'''

'''
class Node:
  def __init__():
    data = ...
    next = ...
'''
    
def removeDuplicatesSinglyLL(lnk_lst):
  prev = lnk_lst.header
  curr = lnk_lst.header.next
  uniqueNodes = {}
  while curr.data is not None:
    # check and move forward
    if curr.data not in uniqieNodes:
      uniqueNodes[curr.data] = curr
      prev = prev.next
      curr = curr.next
    else:
      # disconnect the node
      prev.next = curr.next
      curr = prev.next
      curr.next = None

'''
Test Case:
h -> 1 -> 2 | -> 2 | -> 3 -> t
prev: h, 1, 2, 2, 3
curr: 1, 2, 2, 3, t
uniqueNodes = {1: Node<1>, 2: Node<2>, 3: Node<3>}
'''
