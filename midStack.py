'''
Design a stack with operations on middle element.
  1) push() which adds an element to the top of stack. 
  2) pop() which removes an element from top of stack. 
  3) findMiddle() which will return middle element of the stack. 
  4) deleteMiddle() which will delete the middle element. 
'''

class MidStack:
  
  def __init__(self):
    self.stack = Stack()
    self.middle = Stack()
  
  def push(self, elem):
    # push elem to midstack on odd length
    if len(self.stack) == 0:
        self.middle.push(elem)
    elif len(self.stack) % 2 != 0:
      self.middle.push(self.stack.top())
    # repeat elem for even length
    else:
      self.middle.push(self.middle.top())
    self.stack.push(elem)
    
      
  def pop(self):
    self.middle.pop()
    return self.stack.pop()
  
  def findMiddle(self):
    return self.middle.top()
  
  def deleteMiddle(self):
    pass
  
  
'''
Note: use DoublyLinkedList instead
'''
