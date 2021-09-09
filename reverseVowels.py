class Solution:
    def reverseVowels(self, s: str) -> str:
        str_list = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if str_list[left] in "aeiouAEIOU":
                if str_list[right] in "aeiouAEIOU":
                    temp = str_list[left]
                    str_list[left] = str_list[right]
                    str_list[right] = temp
                    right -= 1
                    left += 1
                else:
                    right -= 1
            else:
                left += 1
        return ''.join(str_list)
            
