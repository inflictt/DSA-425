# 977. Squares of a Sorted Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
nums = [-4,-1,0,3,10]

# optimised - shorter
# # map() har number ko lambda function mein daalega aur square nikalega
# sqs = list(map(lambda x: x**2, nums))

# # Phir un squares ko sort kar do
# return sorted(sqs)

# logner
n = len(nums)
new=[]
for n in nums:
    sq_val = (n)**2
    # sq_val = abs(n)**2
    new.append(sq_val)
print(new)
print(sorted(new))