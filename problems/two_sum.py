"""
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

You may assume that each input has exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
=================
Example 1:
Input: nums = [2, 7, 11, 15], target = 9  
Output: [0, 1]  # Because nums[0] + nums[1] == 9

Example 2:
Input: nums = [3, 2, 4], target = 6  
Output: [1, 2]
"""

def two_sum(nums, target):

    archive = {} # hash map

    for position, num in enumerate(nums):
        complement = target - num

        if complement in archive.keys():
            return [archive[complement], position]
        
        archive[num] = position

    return []

# nums = [3, 3]
# target = 6

# print(two_sum(nums, target))