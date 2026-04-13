def isSubsetSum(self, arr, Sum):

    n = len(arr)
    dp = [[-1 for _ in range(Sum+1)] for i in range(n+1)]  # byb def 0
    # base case ka intial done

    for i in range(0, n+1):  # i-->n-->numbr
        for j in range(0, Sum+1):  # j-->sum-->allowed zeroso True
            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            elif j == 0:
                dp[i][j] = True
    # choice tree ki working k 2 cases include /not incldue and only not include
    for i in range(1, n+1):  # i-->n-->numbr
        for j in range(1, Sum+1):  # j-->sum-->
            if j >= arr[i-1]:  # can pick or ignor
                dp[i][j] = (dp[i-1][j-arr[i-1]] or dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][Sum]
