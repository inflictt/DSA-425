def knapsack(self, W, val, wt):
    # code here
    n = len(wt)
    # size as only the params changing will define th elength of it
    dp = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

    #   base to initalisation
    for i in range(0, n+1):
        for j in range(0, W+1):
            if i == 0 or j == 0:
                dp[i][j] = 0

    for i in range(1, n+1):
        for j in range(1, W+1):
            # include exclude case

            if (j >= wt[i-1]):
                dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
            else:
                dp[i][j] = (dp[i-1][j])
    return dp[n][W]
