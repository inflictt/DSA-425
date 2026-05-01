# def lcs(X, Y):
#     n = len(X)   # rows → X
#     m = len(Y)   # columns → Y

#     dp = [[0 for i in range(m+1)] for j in range(n+1)]

#     # top left and diag i-1 j-1 and j-1
#     for i in range(n):
#         for j in range(m):
#             if X[i] == Y[j]:
#                 # +1 to diag
#                 dp[i+1][j+1] = dp[i][j] + 1
#             else:  # ab ya to upar wala utha lo ya nche ka
#                 dp[i+1][j+1] = max(
#                     dp[i+1][j], dp[i][j+1]
#                 )

#     print("this is n and m", dp[n][m])


# X = "ABCBDEFJIKJ"
# Y = "BACDDBDFPQRFPJKJ"

# lcs(X, Y)

def lcs(X, Y):
    n = len(X)
    m = len(Y)
    dp = [[0 for i in range(m+1)]for j in range(n+1)]
    # if same then dig+1 else:i+1 j and i j+1 all for i+1 and j+1
    for i in range(n):
        for j in range(m):
            if X[i] == Y[j]:  # same
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    print(dp[n][m])


X = "ABCBDEFJIKJ"

Y = "BACDDBDFPQRFPJKJ"
lcs(X, Y)
