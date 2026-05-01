# 3. Floyd Warshall Algorithm
def floyd_warshall(graph):
    # 3 loops in it k i and j and then i j and then i k to k j
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):

                graph[i][j] = min(
                    graph[i][j],
                    graph[i][k] + graph[k][j]
                )
    print("All Pair Shortest Path Matrix:")

    for row in graph:
        print(row)


INF = 99999

graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

floyd_warshall(graph)
