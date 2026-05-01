def dijkstra(graph, src):
    dist = {}
    for vert in graph:
        dist[vert] = float("inf")
    dist[src] = 0
    vis = []

    for u in graph:
        for v, w in graph[u]:
            if dist[u]+w < dist[v]:
                dist[v] = dist[u]+w
    print("Shortest dist is : ", dist)


graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1), ('D', 7)],
    'C': [('D', 3)],
    'D': []
}

dijkstra(graph, 'A')
