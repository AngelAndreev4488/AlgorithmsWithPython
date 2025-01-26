def get_predecessors_count(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1
    return result


def find_node_without_predecessors(predecessors_count):
    for node, count in predecessors_count.items():
        if count == 0:
            return node
    return None


def top_sort(graph, predecessors_count):
    result = []
    while predecessors_count:
        node = find_node_without_predecessors(predecessors_count)
        if node is None:
            break
        for child in graph[node]:
            predecessors_count[child] -= 1
        result.append(node)
        predecessors_count.pop(node)
    return result


nodes = int(input())
graph = {}

for _ in range(nodes):
    line_parts = input().split('->')
    node = line_parts[0].strip()
    children = line_parts[1].strip().split(', ') if line_parts[1] else []
    graph[node] = children

predecessors_count = get_predecessors_count(graph)
sorted_nodes = top_sort(graph, predecessors_count)

if predecessors_count:
    print('Invalid topological sorting')
else:
    print(f"Topological sorting: {', '.join(sorted_nodes)}")


