class Solution:
    def recursion(self, nums, targetSum, n, dp):
        if targetSum == 0:
            return True
        if n == 0:
            return False
        # base cases handled
        if dp[n][targetSum] != -1:
            return dp[n][targetSum]
        # main pick not pick waale cases 2 hai
        if targetSum >= nums[n-1]:
            dp[n][targetSum] = (
                self.recursion(nums, targetSum-nums[n-1], n-1, dp)
                or
                self.recursion(nums, targetSum, n-1, dp)
            )
            return dp[n][targetSum]
        else:
            dp[n][targetSum] = self.recursion(nums, targetSum, n-1, dp)
            return dp[n][targetSum]

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)  # length aagyi
        totalSum = 0
        for val in nums:
            totalSum += val
        ans = 0
        # now we have total sum so we can now have the check
        if totalSum % 2 != 0:
            return False

        else:
            targetSum = totalSum//2
            dp = [[-1 for _ in range(targetSum+1)]for i in range(n+1)]
            ans = self.recursion(nums, targetSum, n, dp)
        return ans
