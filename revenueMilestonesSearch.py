"""
We keep track of the revenue Facebook makes every day, and we want to know on what days Facebook hits certain revenue milestones.
Given an array of the revenue on each day, and an array of milestones Facebook wants to reach,
return an array containing the days on which Facebook reached every milestone.

Example:

revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
milestones = [100, 200, 500]
output = [4, 6, 10]

Ideas:
- keep a running sum and subtract elements from the right side of the array


"""

def getMilestoneDays(revenues, milestones):
  output = []
  runnning_sum = sum(revenues)
  for i in range(len(revenues)):
    rounded_sum = (running_sum // 100) * 100
    if rounded_sum in milestones:
      output.append(len(revenues) - i)
    running_sum -= revenues[-1-i]
  return output


  prefixSum = []
  for revenue in revenues:
    prefixSum.append(revenue)
  def search(target):
    left = 0
    right = len(prefixSum)
    while left < right:
      mid = (left + right) // 2
      if prefixSum[mid] < target:
        left = mid + 1
      else:
        right = mid
    return left if left < len(prefixSum) else -1
  res = []
  for milestone in milestones:
    res.append(search(milestone))
  return res
