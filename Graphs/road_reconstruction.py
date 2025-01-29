def dfs(start, graph, visited):
    if visited[start]:
        return
    visited[start] = True
    for child in graph[start]:
        dfs(child, graph, visited)


number_of_nodes = int(input())
number_of_edges = int(input())

graph = []
edges = []


for _ in range(number_of_nodes):
    graph.append([])

for _ in range(number_of_edges):
    first, second = [int(x) for x in input().split(' - ')]

    graph[first].append(second)
    graph[second].append(first)
    edges.append((min(first, second), max(first, second)))

print(f"Important streets:")

for first, second in edges:
    graph[first].remove(second)
    graph[second].remove(first)

    visited = [False] * number_of_nodes
    dfs(0, graph, visited)

    if not all(visited):
        print(first, second)

    graph[first].append(second)
    graph[second].append(first)
