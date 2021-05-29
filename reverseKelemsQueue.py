'''
Given an integer K and a queue of integers,
we need to reverse the order of the first K elements of the queue,
leaving the other elements in the same relative order.
'''
'''
1. create a helper
2. inside the helper, make a recursive call to queue elements to swap them
'''

# O(n) time and space

def reverseQueue(queue, k):
  low = 0
  high = k - 1
  def helper_reverse_swap(queue, low, high):
    stack = []
    temp_queue = []
    while low < high:
      stack.append(queue.dequeue())
      low -= 1
      high += 1
    while len(queue) != 0:
      temp_queue.enqueue(queue.dequeue())
    while len(stack) != 0:
      queue.enqueue(stack.pop())
    while len(temp_queue) != 0:
      queue.enqueue(temp_queue.dequeue())
    
  
