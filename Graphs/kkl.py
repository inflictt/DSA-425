edges = [
    (4, 0, 1),
    (6, 0, 2),
    (6, 1, 2),
    (3, 1, 3),
    (2, 2, 3)
]

num_vertices = 4
edges.sort()
sel_vert = set()
sel_ed = list()
tc = 0

for w, u, v in edges:
    x, y = u, v
    if not (x in sel_vert and y in sel_vert):
        sel_ed.append((x, y, w))
        sel_vert.add(x)
        sel_vert.add(y)
        tc += w
    print(f"x {x} y {y} with w {w} ")
print(tc, "  = is the ttoal cost")
