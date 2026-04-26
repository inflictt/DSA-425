# Graph input
graph = [
    [0, 4, 3, 0, 0, 0],
    [4, 0, 1, 2, 0, 0],
    [3, 1, 0, 4, 5, 0],
    [0, 2, 4, 0, 2, 3],
    [0, 0, 5, 2, 0, 6],
    [0, 0, 0, 3, 6, 0]
]
numVert = len(graph)
# by default we kept this as we do in diksttra keeping infinity
selected = [False]*numVert
# as this is true my origin to start reaching other node/vbertice
selected[0] = True
for k in range(numVert-1):  # -1 as we need n-1 edges / vertice only following the conditon off mst
    mini = float("inf")
    x, y = 0, 0  # x -> base vertex y-> the vertext x is triyng to reach
    for i in range(numVert):  # base node se ab dusri pr jaane h j tk

        if selected[i] == True:  # agar ye waali base node nhi li toh kese jaayegby j islie
            for j in range(numVert):
                # mtlb self point toh nhi ho rahi checking that
                if selected[j] == False and graph[i][j] != 0:
                    if graph[i][j] < mini:  # toh ye lena hai as anbswer ki ye minimum h
                        mini = graph[i][j]
                        x = i
                        y = j
    print(f"x [{x}] -> y [{y}] is : {graph[x][y]} ")
    selected[y] = True
