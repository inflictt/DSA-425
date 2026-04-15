class Solution:
    def check(self, arr, reqS1, n, dp):

        if n == 0:
            return 1 if reqS1 == 0 else 0
        # only case when we know we can get 1 andrest n Permutcobo are there

        if dp[n][reqS1] != -1:
            return dp[n][reqS1]

        excl = self.check(arr, reqS1, n-1, dp)

        if reqS1 >= arr[n-1]:
            incl = self.check(arr, reqS1-arr[n-1], n-1, dp)
            dp[n][reqS1] = (incl + excl)
            return dp[n][reqS1]

        else:
            dp[n][reqS1] = excl
            return dp[n][reqS1]

    def countPartitions(self, arr, diff):
        # code here
        n = len(arr)
        tSum = 0
        for v in arr:
            tSum += v

        # using the formual Sum(s1) = (diff+TotalSumofArr)//2
        # find the sum(s1)
        if diff > tSum or (diff + tSum) % 2 != 0:
            return 0
        else:
            reqS1 = (diff+tSum)//2

        dp = [[-1 for i in range(reqS1+1)] for j in range(n+1)]
        ans = self.check(arr, reqS1, n, dp)
        return ans
