def ans(wt, profits, capacity):
    ratios = [(profits[i]/wt[i], wt[i], profits[i]) for i in range(len(wt))]
    print(ratios)
    totalP = 0
    ratios.sort(reverse=True)
    for r, w, p in ratios:
        if capacity >= w:
            totalP += p
            capacity -= w
        else:
            totalP += r*capacity
            break
    print(totalP)

    # ratio, wt , profit
items = [
    (7, 49),
    (5, 55),
    (2, 38),
    (9, 27),
    (3, 28)
]
wt = [7, 5, 2, 9, 3]
profits = [49, 55, 38, 27, 28]
capacity = 17
ans(wt, profits, capacity)
