def dfs(i, value):
    for node in value:
        if node not in completed_node:
            completed_node.append(node)
            result[i][node] = 1
            dfs(i, graph[node])

pad_size = int(input())
pad = [list(map(int, input().split())) for _ in range(pad_size)]
graph = {}

result = [list(0 for _ in range(pad_size)) for _ in range(pad_size)]

for i in range(pad_size):
    graph[i] = []
    for j in range(pad_size):
        if pad[i][j] == 1:
            graph[i].append(j)

completed_node = []
for (idx, value) in enumerate(graph.values()):
    completed_node = []
    dfs(idx,value)

for i in range(pad_size):
    print(*result[i])