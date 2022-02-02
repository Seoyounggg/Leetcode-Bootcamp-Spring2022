"""
https://leetcode.com/problems/squares-of-a-sorted-array/

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
non-decreasing order.

"""

# Used two-pointer approach


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        res = [0]*len(nums)
        for idx in range(right,-1,-1):
            if abs(nums[left]) <= abs(nums[right]):
                res[idx] = nums[right]**2
                right -= 1
            else:
                res[idx] = nums[left]**2
                left += 1
        return res
