"""
Given 3 arrays (A, B, C) which are sorted in ascending order, we are required to merge them together in ascending order and output the array D. 
"""

def mergeThreeSortedArrays(A, B, C):
  def mergeTwo(lst1, lst2):
    ind_1 = 0
    ind_2 = 0
    merged = []
    while ind_1 < len(lst1) or ind_2 < len(lst2):
      if lst1[ind_1] <= lst2[ind_2]:
        merged.append(lst1[ind_1])
        ind_1 += 1
      else:
        merged.append(lst2[ind_2])
        ind_2 += 1
    while ind_1 < len(lst1):
      merged.append(lst1[ind_1])
      ind_1 += 1
    while ind_2 < len(lst2):
      merged.append(lst2[ind_2])
      ind_2 += 1
    return merged
  T = merged(A,B)
  return merged(T,C)



      
