class Solution:
    def recursion(self, W, val, wt, n, dp):
        # basecase
        if (n == 0 or W == 0):
            return 0
        if dp[n][W] != -1:
            return dp[n][W]
        # case 1 of W lss than currcurent wt so if no capicty cant add
        if (W < wt[n-1]):  # means we cant add so n-1 only as length toh short hogi
            dp[n][W] = self.recursion(W, val, wt, n-1, dp)
            return dp[n][W]
        else:  # (W>wt[n-1]):#means we can now add and 2 case here of either we take curr or not so max return hoga
            dp[n][W] = (max
                        (val[n-1]+self.recursion(W-wt[n-1], val, wt, n-1, dp), self.recursion(W, val, wt, n-1, dp)))
            return dp[n][W]

    def knapsack(self, W, val, wt):
        # code here
        n = len(wt)
        # size as only the params changing will define th elength of it
        dp = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]
        return self.recursion(W, val, wt, n, dp)
