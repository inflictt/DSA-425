# 905. Sort Array By Parity

# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

 

# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

nums = [3,1,2,4]
left = 0
# approach -ek start pointer bana liya, jaise hi even aaya usko start par phenk diya, aur start wale ko i par
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        nums[left], nums[i] = nums[i], nums[left]
        left += 1

print (nums)