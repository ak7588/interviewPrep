"""
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions.
Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

Algorithm:
1. create a dubplicated sorted array
2. run through both arrays at the same time to compare elements
3. if some elements stayed in place, then they have ocean view
"""

def findBuildings(heights):
  output = []
  duplicates = [elem for elem in heights]
  duplicates = duplicates.sort(reversed = True)
  for i in range(len(heights)):
    if duplicates[i] == heights[i]:
      output.append(i)
    elif:
      duplicates[i] > heights[i]:
        output.append(i)
  return output
