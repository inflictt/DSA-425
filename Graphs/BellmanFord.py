# def bellman_ford(vertices, edges, source):
#     # make rc and rest 0 and inf respectively
#     distance = {}
#     for vert in vertices:
#         distance[vert] = float("inf")
#     distance[source] = 0

#     # now relax
#     for i in range(len(vertices) - 1):
#         for u, v, w in edges:
#             if distance[u] != float("inf") and distance[u]+w < distance[v]:
#                 distance[v] = distance[u] + w

#     for vertex in distance:
#         print(vertex, " is ", distance[vertex])


# vertices = ['A', 'B', 'C', 'D']

# edges = [
#     ('A', 'B', 4),
#     ('A', 'C', 5),
#     ('B', 'C', -2),
#     ('B', 'D', 6),
#     ('C', 'D', 3)
# ]

# source = 'A'

# bellman_ford(vertices, edges, source)
# # make dict distance then vertex to be set inf then src to be 0 then relax these vertice v-1 then u,v,w abd check dist[u]+w < dist[v] then dist[v] = dist[u]+w


def ans(vert, edges, src):
    dist = {}
    for v in vert:
        dist[v] = float("inf")
    dist[src] = 0
    for i in range(len(vert)-1):
        for u, v, w in edges:
            if dist[u]+w < dist[v]:
                dist[v] = dist[u]+w
    print("dist is ; ", dist)


vertices = ['A', 'B', 'C', 'D']

edges = [
    ('A', 'B', 4),
    ('A', 'C', 5),
    ('B', 'C', -2),
    ('B', 'D', 6),
    ('C', 'D', 3)
]

source = 'A'
ans(vertices, edges, source)
