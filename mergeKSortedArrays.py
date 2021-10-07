def mergeKArrays(k, n, lst):
  ind_1 = ind_2 = ind_3 = 0
  output = []
  out1 = []
  out2 = []
  def mergeTwoArrays(lst1, lst2):
    i = j = 0
    while i < len(lst1) or j < len(lst2):
      if lst1[i] < lst2[j]:
        output.append(lst1[i])
        i += 1
      elif lst1[i] > lst2[j]:
        output.append(lst2[j])
        j += 1
      else:
        output.append(lst1[i])
        i += 1
        j += 1
    while i < len(lst1):
      output.append(lst1[i])
      i += 1
    while j < len(lst2):
      output.append(lst2[j])
      j += 1
      
  def mergeUntilOneLeft(lst, i, j, output):
    if i == j:
      for elem in lst[][]:
        output.append(elem)
      return
    if j - i == 1:
      mergeTwoArrays(i, j)
      return
    mergeUntilOneLeft(arr,i,(i+j)/2,out1);
    mergeUntilOneLeft(arr,(i+j)/2+1,j,out2);
    mergeUntilOneLeft(out1,out2,n*(((i+j)/2)-i+1),n*(j-((i+j)/2)),output);
    
    
    
