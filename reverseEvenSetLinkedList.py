"""
You are given a singly-linked list that contains N integers. 
The goal of this question is: given a resulting list, determine the original order of the elements.

0. Iterate
0.1. If curr.next = even and curr.next.next = even
0.2. Swap


Reversing:
  temp = curr.next
  curr.next = curr.next.next
  curr.next.next = temp
  
"""

def reverse(head):
  curr = head
  while curr:
    if curr.data % 2 == 0 and curr.next.data % 2 == 0:
      temp = curr.next
      curr.next = curr.next.next
      curr.next.next = temp
    curr = curr.next
   return head
      
  
