
def minDifference(self, arr):
    # code here
    n = len(arr)
    totalSum = 0
    for i in arr:
        totalSum += i
    targetSum = totalSum//2  # givesd rthe pivot target sum we need to alculate x
    dp = [[False for _ in range(targetSum+1)]for i in range(n+1)]
    for i in range(0, n+1):
        for j in range(0, targetSum+1):

            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            elif j == 0:
                dp[i][j] = True

    for i in range(1, n+1):
        for j in range(1, targetSum+1):

            if j >= arr[i-1]:
                dp[i][j] = (dp[i-1][j-arr[i-1]]
                            or (dp[i-1][j])
                            )
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp)
    req = dp[-1]
    mini = float('inf')
    for i in range(targetSum+1):  # range -2*S[i]
        if req[i] == True:  # only valdi allowed
            mini = min(mini, totalSum-(2*i))

    return mini
