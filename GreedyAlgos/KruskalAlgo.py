# Kruskal's Algorithm using edge list input

# Each edge is represented as:
# (weight, vertex1, vertex2)
# Kruskal's Algorithm (your way)

edges = [
    (4, 0, 1),
    (6, 0, 2),
    (6, 1, 2),
    (3, 1, 3),
    (2, 2, 3)
]

num_vertices = 4

# Step 1: Sort edges by weight
edges.sort()

selected_vertices = set()
selected_edges = []

for wt, x, y in edges:

    # take edge if both vertices are not already fully selected together
    if not (x in selected_vertices and y in selected_vertices):

        selected_edges.append((wt, x, y))

        selected_vertices.add(x)
        selected_vertices.add(y)

    if len(selected_edges) == num_vertices - 1:
        break

print("Selected Edges =", selected_edges)
print("Selected Vertices =", selected_vertices)

total_cost = 0
for wt, x, y in selected_edges:
    total_cost += wt

print("Total Cost =", total_cost)
