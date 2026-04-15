class Solution:
    def recur(self, nums, req, n, dp):

        if n == 0:  # only case where we know the exact val of elem in dp also the base case
            dp[n][req] = 1 if req == 0 else 0
            return dp[n][req]

        if dp[n][req] != -1:
            return dp[n][req]

        exclude = self.recur(nums, req, n-1, dp)
        if req >= nums[n-1]:
            include = self.recur(nums, req-nums[n-1], n-1, dp)
            dp[n][req] = include+exclude
            return dp[n][req]

        else:
            dp[n][req] = exclude
            return dp[n][req]

    def findTargetSumWays(self, nums, target):
        n = len(nums)
        tsum = 0
        for val in nums:
            tsum += val
        # boundeary check krli what all possible in which ans might not come as expected when target he bada ho toh kese aaayega
        if abs(target) > tsum:
            return 0
        # agar target +total jo required hai woh eh odd aajaye toh point k issues aayengye so 0
        if (tsum+target) % 2 != 0:  # mtlb odd h retu 0
            return 0
        # from prev knowledge we required this S1+S2 is TotallSum of arr and S1-S2 is diffrence jo ki requried then doing lhs rhs a bit we got the formula
        req = (tsum+target)//2
        dp = [[-1 for i in range(req+1)]for j in range(n+1)]

        ans = self.recur(nums, req, n, dp)
        return ans
