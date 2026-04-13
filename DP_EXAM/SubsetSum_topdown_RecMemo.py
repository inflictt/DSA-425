class Solution:
    def check(self, arr, Sum, n, dp):
        # bc is this ki ko.n true hopayega at lowest and kon nhi
        if Sum == 0:  # sum is cols and cols incraase at 0 but cant have a empty arr
            return True
        if n == 0:
            return False

        if dp[n][Sum] != -1:
            return dp[n][Sum]

        # main 2 cases one is include/not inc and otheris stric not incd
        if arr[n-1] <= Sum:  # we can pick and not picl
            dp[n][Sum] = (self.check(arr, Sum-arr[n-1], n-1, dp)
                          or self.check(arr, Sum, n-1, dp))
            return dp[n][Sum]
        else:  # bada hai sum se
            dp[n][Sum] = self.check(arr, Sum, n-1, dp)
            return dp[n][Sum]

    def isSubsetSum(self, arr, Sum):
        # code here
        n = len(arr)
        dp = [[-1 for _ in range(Sum+1)]for i in range(n+1)]  # byb def 0
        return self.check(arr, Sum, n, dp)
