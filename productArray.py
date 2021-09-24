"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

array slicing from 0...n
"""

def productExceptSelf(self, nums: List[int]) -> List[int]:
    output = [1] * len(nums)
    L = len(output)
    for i in range(1,L):
        output[i] = output[i-1] * nums[i-1]
    r = 1
    for i in reversed(range(L)):
        output[i] = output[i] * r
        r = r * nums[i]
    return output
