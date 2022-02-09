"""
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and
numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

# Using two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left <= right:
            l, r = s[left].lower(), s[right].lower()
            if l.isalnum() and r.isalnum():
                if l != r:
                    return False
                else:
                    left += 1
                    right -= 1
                    continue
            left, right = left + (not l.isalnum()), right- (not r.isalnum())
        return True

# Using list slicing
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = ""
        for s_ in s:
            if s_.isalnum():
                s_lower += s_.lower()
        if s_lower == s_lower[::-1]:
            return 1
        else:
            return 0