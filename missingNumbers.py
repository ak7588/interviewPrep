class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dict_count = {}
        for i in range(len(nums)+1):
            dict_count[i] = 1
        for i in range(len(nums)):
            if nums[i] in dict_count:
                dict_count[nums[i]] += 1
        for key, val in dict_count.items():
            if val == 1:
                return key
