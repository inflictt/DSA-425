# 215. Kth Largest Element in an Array
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?


# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
from typing import List
import random

nums = [3, 2, 1, 5, 6, 4]
k = 2


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def DNF_QS(nums, left, equal, right):
            left, equal, right = left, equal, right
            pivot = nums[random.randint(left, right)]

            while equal <= right:
                # put to left ans left contain elm bigger than pivot means do swap
                if nums[equal] > pivot:
                    nums[left], nums[equal] = nums[equal], nums[left]
                    left += 1
                    equal += 1

                # means 3 < pivot so put this to right as in right all smll elem
                elif nums[equal] < pivot:
                    nums[right], nums[equal] = nums[equal], nums[right]
                    right -= 1

                else:  # ab toh ye phir equal he hai toh +=1
                    equal += 1

            return left, right

        # so equal index start se piche sare bade elem hongey
        # and right to equal_Index_ending mai all small elm hongey

        targetIndex = k - 1   # as 0th indexing arr
        left, right = 0, len(nums) - 1

        while True:
            equal_Index_starting, equal_Index_ending = DNF_QS(
                nums, left, left, right
            )

            # now check where target index lies
            if targetIndex < equal_Index_starting:  # check left
                right = equal_Index_starting - 1

            elif targetIndex > equal_Index_ending:  # check right
                left = equal_Index_ending + 1

            else:
                return nums[equal_Index_starting]


# ✅ driver code for VS Code
sol = Solution()
ans = sol.findKthLargest(nums, k)
print("Kth largest element is:", ans)
