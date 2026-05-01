def ans(graph):
    V = len(graph)

    for k in range(V):
        for i in range(V):
            for j in range(V):
                # ij min or itok and k to i
                graph[i][j] = min(graph[i][j],
                                  graph[i][k]+graph[k][j])

    print("finl graph")
    for r in graph:
        print(r)


INF = 99999

graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]
ans(graph)
