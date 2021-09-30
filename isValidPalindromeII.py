"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

-> Empty string: just return in that case?
-> Same chars in the str?
-> Are all chars valid/alpha? 

Algorithm:
1. Two pointers, left = 0, right = len(s) - 1
2. Iterating over s and compare s[left] and s[right]
2.1. while left < right, increment and decrement after every iteration respectively
3. Initialize a variable that keeps track of how many times a char was skipped because it wasn't equal to one of the pointers
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return False
        
        def isPalindrome(s):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False, left, right
                else:
                    left += 1
                    right -= 1
            return True, 0, len(s) - 1
        
        res, i, j = isPalindrome(s)
        if res:
            return True
        
        res, _, _ = isPalindrome(s[:i] + s[i+1:])
        if res:
            return True
        
        res, _, _ = isPalindrome(s[:j] + s[j+1:])
        if res:
            return True
        
        return False
