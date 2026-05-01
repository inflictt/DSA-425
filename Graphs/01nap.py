def ans(wt, profit, W):
    n = len(wt)
    dp = [[0 for i in range(W+1)]for j in range(n+1)]
    for i in range(1, n+1):
        for Cap in range(1, W+1):
            if Cap >= wt[i-1]:
                dp[i][Cap] = max(profit[i-1]+dp[i-1]
                                 [Cap-wt[i-1]], dp[i-1][Cap])
            else:
                dp[i][Cap] = dp[i-1][Cap]
    print(dp[n][W])


weights = [2, 5, 7, 4, 8, 3, 9]

profits = [8, 14, 21, 10, 16, 18, 8]

capacity = 11
ans(weights, profits, capacity)
