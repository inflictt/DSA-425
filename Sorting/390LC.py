# 442. Find All Duplicates in an Array
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
nums = [4,3,2,7,8,2,3,1]
hashMap = {}
for num in range(len(nums)):
    hashMap[nums]=hashMap.get(num,0)+1