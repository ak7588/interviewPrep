"""
You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:
- The value at index i must be the maximum element in the contiguous subarrays, and
- These contiguous subarrays must either start from or end on index i.

Edge-cases: can it be an empty array? array of one element? Or an array where all of the elements are equal to each other? 

arr[i] = max

[..., ..., arr[i]]
[arr[i], ..., ...]

1. Slicing the array into left-arr[i] and arr[i]-right
2. for left_ind loop that runs from 0 to arr[i]
   2.0 if arr[left_ind] < arr[i]
      2.1. create subarrays that start with arr[left_ind] and arr[i]
3. for right_ind loop from arr[i] to len(arr)-1
   3.0 if arr[i] > arr[right_ind]
      3.1. create subarrays that start with arr[i] and end with arr[right_ind]
4. count the number of subarrays for each index
5. return that sum

first elements i need to check are arr[i-1] and arr[i+1]

"""

def count_subarrays(arr):
  subarrays = []
  for index in range(len(arr)-1):
    subarrays_count = 1
    if index > 0:
      left_ind = 0
      right_ind = index
      while arr[left_ind] < arr[index]:
        subarrays_count += 1
      while arr[index] > arr[right_ind]
        subarrays_count += 1
    subarrays.append(subarrays_count)
  return subarrays
          
          
          
        
  
