'''
Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.
'''

def are_they_equal(array_a, array_b):
  return array_a.sorted() == array_b.sorted()
  
