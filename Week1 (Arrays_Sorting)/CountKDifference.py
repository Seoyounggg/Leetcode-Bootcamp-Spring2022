"""
https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] -
nums[j]| == k.

"""

# Using hashmap
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res_dict = {}
        res = 0
        for num in nums:
            if num in res_dict:
                res_dict[num] += 1
            else:
                res_dict[num] = 1
        for num in nums:
            if num + k in res_dict:
                res += res_dict[num+k]
        return res
