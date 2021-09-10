def moveZeroes(nums):
  if len(nums) == 0:
    return
	right = 0
	for i in range(len(nums)):
		if nums[i] != 0:
			swap(nums[i], nums[right])
			right += 1
	return nums	
