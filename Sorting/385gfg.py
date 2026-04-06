# Difficulty: MediumAccuracy: 16.93%Submissions: 766K+Points: 4
# Given an array of integers arr[]. You have to find the Inversion Count of the array. 
# Note : Inversion count is the number of pairs of elements (i, j) such that i < j and arr[i] > arr[j].

# Examples:

# Input: arr[] = [2, 4, 1, 3, 5]
# Output: 3
# Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

class Solution:
    def inversionCount(self, arr):

        def mergeCombine(leftArr, rightArr):
            n = len(leftArr)
            m = len(rightArr)

            res = []
            ans = 0
            i, j = 0, 0

            # merge both sorted halves
            while i < n and j < m:
                if leftArr[i] <= rightArr[j]:
                    res.append(leftArr[i])
                    i += 1
                else:
                    # all remaining elements in leftArr
                    # will be greater than rightArr[j]
                    ans += n - i
                    res.append(rightArr[j])
                    j += 1

            # append leftover left half
            while i < n:
                res.append(leftArr[i])
                i += 1

            # append leftover right half
            while j < m:
                res.append(rightArr[j])
                j += 1

            # return merged sorted array + inversion count
            return res, ans

        def mergeSort(nums):
            # base case
            if len(nums) <= 1:
                return nums, 0

            mid = len(nums) // 2

            leftArr = nums[:mid]
            rightArr = nums[mid:]

            # recursively sort both halves
            leftSorted, leftCount = mergeSort(leftArr)
            rightSorted, rightCount = mergeSort(rightArr)

            # count cross inversions while merging
            merged, crossCount = mergeCombine(leftSorted, rightSorted)

            # total = left + right + cross
            return merged, leftCount + rightCount + crossCount

        # only return inversion count
        _, totalInversions = mergeSort(arr)
        return totalInversions