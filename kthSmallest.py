'''
Given an array arr[] and a number K where K is smaller than size of array,
the task is to find the Kth smallest element in the given array.
It is given that all array elements are distinct.
'''

'''
1) sort the array
2) get the kth element

but that would require some time complexity for sorting, which in best case is O(nlogn) with mergeSort and time complexity for recursion used.
there is a quicker way to do it utilizing partition but i am not entirely familiar with it, so i would start off with the method proposed above
and if there is a room for optimization later, I will do it.

1. define a helper to merge sort
2. return lst[k]

'''

# Initial Solution

def k_th_smallest(k, lst):
  low = 0
  high = len(lst) - 1
  def merge_sort(lst, low, high):
    if len(lst) == 0 or len(lst) == 1:
      return
    else:
      left = merge_sort(lst, (low + high)//2, high)
      right = merge_sort(lst, 0, (low + high)//2)
      for i in range(min(len(left), len(right)):
        if left[i] > right[i]:
          lst[i] = right[i]
        elif right[i] > left[i]:
          lst[i] = left[i]
        else: # =
          lst[i] = left[i]
      if len(left) > len(right):
        for i in range(len(right), len(left)):
          lst[i] = left[i]
      elif len(right) > len(left):
          lst[i] = right[i]
      return lst
   return merge_sort(lst, low, high)[k-1]
      
# Comment: might have errors will come back tomorrow to fix
                     
# Corrected Solution
def k_th_smallest(k, l, r, lst):
   if k > 0 and k <= r - l + 1:
       pos = partition(lst, l, r)
       if pos - l == k - 1:
          return lst[pos]
       elif pos - l > k - 1:
          return k_th_smallest(k, l, pos - 1, lst)
       return k_th_smallest(k - pos + l - 1, pos + 1, r, lst)
   def partition(lst, left, right):
       index = left
       for i in range(left, right):
           if lst[i] <= lst[right]:
               lst[index], lst[i] = lst[i], lst[index]
               index += 1
       lst[index], lst[right] = lst[right], lst[index]
       return index
                     

