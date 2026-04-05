# 179. Largest Number
# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

# Example 1:

# Input: nums = [10,2]
# Output: "210"
# Input: nums = [3,30,34,5,9]
# Output: "9534330
nums = [3,30,34,5,9]
# ill be solving using custom sort 
# make the list of int into a list of strings
from functools import cmp_to_key
for i , n in enumerate(nums):
    nums[i]=str(n)
    #converted to ["10","2"] 
#make compare functiopn for comaprator

def compare(n1,n2):
    if n1+n2 > n2+n1:  # mtlb n1 bada aur aage aana chahye A in front of B means ret -1
        return -1
    if n1+n2 < n2+n1:
        return 1
    return 0

nums = sorted(nums, key=cmp_to_key(compare))
ans =  str(int("".join(nums)))

print(ans)

# algo behing cmp_to_key
# It grabs two elements at a time (your n1 and n2).

# It feeds them into your compare function.

# Based on the -1 or 1 answer, it updates their positions in the array.

# It keeps iterating over nums, picking new pairs, and moving things around until no more updates are needed.