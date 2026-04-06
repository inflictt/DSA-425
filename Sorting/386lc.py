# 493. Reverse Pairs
# Given an integer array nums, return the number of reverse pairs in the array.

# A reverse pair is a pair (i, j) where:

# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j].
 

# Example 1:

# Input: nums = [1,3,2,3,1]
# Output: 2
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
nums = [1,3,2,3,1]
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeCombine(leftArr,rightArr,mid):
            n= len(leftArr)
            m= len(rightArr)
            res = []
            count=0
            #  PHASE 1: count reverse pairs first
            j = 0
            for i in range(n):
                while j < m and leftArr[i] > 2 * rightArr[j]:
                    j += 1
                count += j
            #  PHASE 2: normal merge sort merge
            i,j = 0, 0
            while i<n and j<m:
                if leftArr[i]<rightArr[j]:
                    res.append(leftArr[i])
                    i+=1
                else :
                    res.append(rightArr[j])
                    j+=1
            if i<n :
                while i<n:
                    res.append(leftArr[i])
                    i+=1
            if j<m :
                while j<m:
                    res.append(rightArr[j])
                    j+=1
            return res,count

        def mergeSort(nums):
            if len(nums)<=1:return nums,0

            n = len(nums)
            mid= n//2
            leftPart = nums[:mid]
            rightPart = nums[mid:]

            leftArr,leftCount = mergeSort(leftPart)#left part ka ans
            rightArr,rightCount = mergeSort(rightPart)#right part ka ans
            merged, crossCount = mergeCombine(leftArr ,  rightArr,mid) #main sorteed dono ka ans
            return  merged ,leftCount+rightCount+crossCount 
        arr , ans= mergeSort(nums)
        return ans