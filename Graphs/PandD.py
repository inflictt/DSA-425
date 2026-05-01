# def ans(graph, start):
#     dist = {}

#     # Step 1: initialize all distances as infinity
#     for node in graph:
#         dist[node] = float('inf')

#     # Step 2: source node distance = 0
#     dist[start] = 0

#     # visited nodes list
#     vis = []

#     # Step 3: run for all nodes
#     for _ in range(len(graph)):

#         # find minimum distance unvisited node
#         min_node = None
#         min_dist = float('inf')

#         for node in graph:
#             if node not in vis and dist[node] < min_dist:
#                 min_dist = dist[node]
#                 min_node = node

#         # if no node found, stop
#         if min_node is None:
#             break

#         # mark node as visited
#         vis.append(min_node)

#         # Step 4: relax neighbours of min_node only
#         for v, w in graph[min_node]:
#             if dist[min_node] + w < dist[v]:
#                 dist[v] = dist[min_node] + w

#     print(dist)


# graph = {
#     'A': [('B', 3), ('C', 1), ('E', 5)],
#     'B': [('A', 3), ('C', 4), ('D', 3), ('G', 7)],
#     'C': [('A', 1), ('B', 4), ('D', 2)],
#     'D': [('B', 3), ('C', 2), ('E', 4), ('G', 6)],
#     'E': [('A', 5), ('D', 4), ('F', 2)],
#     'F': [('E', 2)],
#     'G': [('B', 7), ('D', 6)]
# }

# start = 'E'
# ans(graph, start)

# -------Prims------#
# Prim's Algorithm (Easy Version)

# Graph represented using adjacency matrix
graph = [
    [0, 2, 3, 4, 5, 6],
    [7, 0, 9, 10, 11, 12],
    [13, 14, 0, 16, 17, 18],
    [19, 20, 21, 0, 23, 24],
    [25, 26, 27, 28, 0, 30],
    [31, 32, 33, 34, 35, 0]
]

# Total number of vertices
n = len(graph)

# Keep track of visited/selected vertices
selected = [False] * n

# Start from vertex 0
selected[0] = True

# To store final MST cost
total_cost = 0

# MST always has (n - 1) edges
for _ in range(n - 1):

    # Initially minimum edge weight = infinity
    mini = float('inf')

    # x = starting vertex
    # y = ending vertex
    x = 0
    y = 0

    # Traverse all vertices
    for i in range(n):

        # Only check from already selected vertices
        if selected[i]:

            # Check all possible connected vertices
            for j in range(n):

                # Condition:
                # 1. j should not be selected already
                # 2. weight should not be 0 (self-loop)
                if not selected[j] and graph[i][j] != 0:

                    # Find minimum edge
                    mini = min(mini, graph[i][j])

                    # If current edge is minimum, store it
                    if mini == graph[i][j]:
                        x = i
                        y = j

    # Print selected edge
    print(x, "->", y, "=", graph[x][y])

    # Add edge weight to total MST cost
    total_cost += graph[x][y]

    # Mark new vertex as selected
    selected[y] = True

# Final minimum spanning tree cost
print("Total Cost =", total_cost)
