# Implementing solutions for 0/1-Knapsack problem using Dynamic Programming
# Input:  W = 4, val[] = [1, 2, 3], wt[] = [4, 5, 1]
# Output: 3

W = 4  # Max capacity
val = [1, 2, 3]  # Values of corresponding weights
wt = [4, 5, 1]   # Weights of the items
n = len(wt)

# Initialize the DP table with 0s.
# This handles the base cases (i=0 or j=0) automatically, saving us a loop!
dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

# Fill the DP table bottom-up
for i in range(1, n + 1):
    for j in range(1, W + 1):

        excl = dp[i-1][j]  # Value if we EXCLUDE the current item

        # Check if the current item's weight fits in the current capacity 'j'
        if j >= wt[i-1]:
            incl = val[i-1] + dp[i-1][j - wt[i-1]]  # Value if we INCLUDE it
            dp[i][j] = max(incl, excl)
        else:
            dp[i][j] = excl  # Too heavy, must exclude

print(f"Maximum possible value: {dp[n][W]}")
