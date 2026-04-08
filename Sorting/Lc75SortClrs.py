class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket_size = 3 
        buckets = [[] for _ in range(bucket_size)]
        
        # 1. Scatter (Time: O(N))
        for num in nums:
            buckets[num].append(num)
        ans = []
        
        # 2. Gather (Time: O(N))
        for bucket in buckets:
            ans.extend(bucket)
        nums[:] = ans
