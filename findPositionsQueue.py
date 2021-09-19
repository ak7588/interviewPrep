"""
You're given a list of n integers arr, which represent elements in a queue (in order from front to back).
You're also given an integer x, and must perform x iterations of the following 3-step process:

1.Pop x elements from the front of queue (or, if it contains fewer than x elements, pop all of them)
2.Of the elements that were popped, find the one with the largest value (if there are multiple such elements, take the one which had been popped the earliest), and remove it
3.For each one of the remaining elements that were popped (in the order they had been popped), decrement its value by 1 if it's positive (otherwise, if its value is 0, then it's left unchanged), and then add it back to the queue

original queue
output queue: an array of indeces of max elements from each iteration

1. create a dictionary of {arr[i]: i}
2. iterate through elements to pop
3. store popped elements only if it's greater then the other
4. for values that are > 0, decrement and enqueue them back to the queue
5. append the popped value's index to the output array

"""

def findPositions(arr, x):
  
  # internal function
  def removeMaxAndDecrementOthers(arr, n, index):
    for i in range(n):
        temp_1 = arr.pop()
        temp_2 = arr.pop()
        if temp_1 >= temp_2:
          outputp[index] = index_dict[temp_1]
          if temp_2 >= 0:
            temp_2 -= 1
          arr.append(temp_2)
        else:
          outputp[index] = index_dict[temp_2]
          if temp_1 >= 0:
            temp_1 -= 1
          arr.append(temp_1)
  
  # edge cases
  if len(arr) == 0:
    return 0
  if len(arr) == 1:
    return 0
  
  # space
  index_dict = {}
  output = [0 for i in range(len(arr))]
  temp_storage = []
  
  # keep track of indeces for the output
  for i in range(len(arr)):
    index_dict[arr[i]] = i
    
  while len(arr) != 0:
    count = 0
    if len(arr) >= x:
      removeMaxAndDecrementOthers(arr, x, count)
      count += 1
     else:
      removeMaxAndDecrementOthers(arr, len(arr), count)
      count += 1
      
      
---

def correct_solution(arr, x):
  queue = [(elem, pos+1) for elem, pos in enumerate(arr)]
  output = []
  for i in range(x):
    temp = queue[:x]
    max_elem = max(temp)
    output.append(max_elem[1])
    temp.remove(max_elem)
    temp = [(elem-1, pos) if elem > 0 else (elem, pos) for elem, pos in temp]
    queue = queuep[x:] + temp
  return output
  
  
  
