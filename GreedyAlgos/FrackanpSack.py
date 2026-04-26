# Implementing Greedy algorithms to solve Fractional knapsack
# problem and do the time complexity analysis.
# Input:
# val = [60, 100, 120]
# wt = [10, 20, 30]
# capacity = 50

# Output: 240.0
# Explanation:
# - Pick item2 (value=100, weight=20) fully → remaining capacity = 30
# - Pick item3 (value=120, weight=30) fully → remaining capacity = 0
# Total value = 100 + 120 = 220

# But better choice:
# - Pick item1 (value=60, weight=10) fully → remaining capacity = 40
# - Pick item2 (value=100, weight=20) fully → remaining capacity = 20
# - Pick 2/3 fraction of item3 (value=120, weight=30) → add 80
# Total value = 60 + 100 + 80 = 240

def FracKnap(W, wt, val):
    final_profit = 0
    n = len(wt)  # get the numbr of weight we have to itr over
    #  find ratios
    # so htsi si my (profit upon wt ratio , wts , vals )
    ratios = [(val[i]//wt[i], wt[i], val[i]) for i in range(0, n)]
    # Step 2: sort in descending order of ratio
    ratios.sort(reverse=True, key=lambda x: x[0])

    # now itr witha. loop over ratio,wts ,profits
    for r, w, p in ratios:
        if W >= w:
            final_profit += p
            W -= w
        else:
            final_profit += r * W
            break  # as knaop sack si full
    return final_profit


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
max_profit = FracKnap(W, wt, val)
print("The max profit of this will be : ", max_profit)
