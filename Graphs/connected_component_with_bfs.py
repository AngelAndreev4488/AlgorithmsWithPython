from collections import deque


def bfs(node, graph, visited, component):
    queue = deque([node])
    visited[node] = True
    while queue:
        current = queue.popleft()
        component.append(current)
        for child in graph[current]:
            if not visited[child]:
                visited[child] = True
                queue.append(child)


nodes = int(input("Enter the number of nodes: "))
graph = []

for _ in range(nodes):
    children = [int(x) for x in input().split()]
    graph.append(children)

visited = [False] * nodes

for node in range(nodes):
    if visited[node]:
        continue
    component = []
    bfs(node, graph, visited, component)
    print(f"Connected component: {' '.join([str(x) for x in component])}")
