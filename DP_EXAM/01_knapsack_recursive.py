class Solution:
    def knapsack(self, W, val, wt):
        # code here
        def recursion(W, val, wt, n):
            # basecase
            if (n == 0 or W == 0):
                return 0
            # case 1 of W lss than currcurent wt so if no capicty cant add
            if (W < wt[n-1]):  # means we cant add so n-1 only as length toh short hogi
                return recursion(W, val, wt, n-1)
            else:  # (W>wt[n-1]):#means we can now add and 2 case here of either we take curr or not so max return hoga
                return (max
                        (val[n-1]+recursion(W-wt[n-1], val, wt, n-1)), recursion(W, val, wt, n-1))

        n = len(wt)
        return recursion(W, val, wt, n)
