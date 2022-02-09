"""
https://leetcode.com/problems/valid-palindrome-ii/

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

"""

# Using two pointers
class Solution(object):
    def validPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                cut_right, cut_left = s[left:right], s[left + 1:right + 1]
                return cut_right == cut_right[::-1] or cut_left == cut_left[::-1]
            left, right = left + 1, right - 1
        return True