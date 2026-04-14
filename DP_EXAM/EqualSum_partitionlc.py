class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)  # length aagyi
        totalSum = 0
        for val in nums:
            totalSum += val
        ans = 0
        # now we have total sum so we can now have the check
        if totalSum % 2 != 0:
            return False

        dp = [[False for _ in range(totalSum+1)]for o in range(n+1)]
        # as now the problem is reduce to subset sum only finding the sum//2 is the case here
        targetSum = totalSum//2
        for i in range(0, n+1):  # i->n which th len
            for j in range(0, targetSum+1):  # j points to target - > total/2
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = False
                elif j == 0:
                    dp[i][j] = True
                # matirs made and initlsed with base conditon of top down
        # now iterative which was recursive in top down having 2 cases and staritng from as  0 is being initlaised
        for i in range(1, n+1):  # i->n which th len
            for j in range(1, targetSum+1):  # j points to target - > total/2

                # main case 1 take not take in this using or        #
                if j >= nums[i-1]:  # lo mt lo 2 choices h
                    dp[i][j] = ((dp[i-1][j-nums[i-1]])
                                or
                                (dp[i-1][j])
                                )
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][targetSum]
