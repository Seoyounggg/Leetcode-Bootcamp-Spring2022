"""
https://leetcode.com/problems/intersection-of-two-arrays/

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be
unique and you may return the result in any order.

"""

# Using dictionary
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_dict, res = {}, []

        for num in nums1:
            if num not in num_dict:
                num_dict[num] = 1

        for num in nums2:
            if num in num_dict and num_dict[num] != 2:
                num_dict[num] += 1

        for key, value in num_dict.items():
            if value == 2:
                res.append(key)

        return res


# Using set
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)