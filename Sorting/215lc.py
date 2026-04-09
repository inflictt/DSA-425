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
# using pq and min heap
import heapq
nums = [3,2,1,5,6,4]
k = 2
ans =[]
n=len(nums)
for i in range(k):
    heapq.heappush(ans,nums[i])#makes an ans arr already sorted as heapq min heap manner and  utne add kiye jitne kth largest required jese k=3 to onlyfrist 3 elem thenm k to n we looped to check for other 

for i in range(k,n):
    if nums[i]>ans[0]:
        heapq.heappop(ans)#if not the largest in top of ans thenswap means pop top of and and add nums[i] in there
        heapq.heappush(ans,nums[i])#add the latest nums[i] in there and returnt top most elem which  is 0 index
print (ans[0])
