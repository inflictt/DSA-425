def mcm(arr):
    n = len(arr)
    dp = [[0 for i in range(n)]for j in range(n)]
    for l in range(2, n):
        for i in range(1, n-l+1):
            j = i+l-1
            dp[i][j] = float("inf")
            for k in range(i, j):
                cost = dp[i][k]+dp[k+1][j]+arr[i-1]*arr[k]*arr[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    print(dp[1][n-1])


arr = [10, 20, 30, 40]

mcm(arr)
