"""
Given a list of intervals [ [6,7], [2,5], [0,2], [7,8], [7,10] ], merge overlapping intervals so the result in this case would be [ [0,5], [6,10] ]

[[0,2], [2,5], [6,7], [7,8], [7,10]]
[[0,5], [6,8], [7,10]]
[[0,5], [6,10]]
"""

def mergeIntervals(intervals):
  output = []
  intervals.sort(key = lambda interval: interval[0] + interval[1])
  i = 0
  j = i + 1
  while j < len(intervals) - 1:
     if interval[i][1] >= interval[j][0]:
        interval[i][1] = interval[j][1]
        intervals.delete(interval[j])
        j += 1
     else:
      i += 1
      j += 1
  return intervals
        
    
    
  
