def ans(p):
    n = len(p)
    dp = [[0 for i in range(n)]for i in range(n)]
    for l in range(2, n):
        for i in range(1, n-l+1):
            j = i+l-1
            dp[i][j] = float("inf")
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j]+p[i-1]*p[k]*p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    print(dp[i][n-1])


p = [12, 6, 4, 9, 20, 50, 8, 5, 30, 10]
ans(p)
