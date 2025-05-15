def is_safe(node, color, assignment, graph):
    for neighbor in graph[node]:
        if assignment.get(neighbor) == color:
            return False
    return True

def map_coloring(graph, colors, assignment={}, node=0, nodes=None):
    if nodes is None:
        nodes = list(graph.keys())
    if node == len(nodes):
        return assignment
    
    current = nodes[node]
    for color in colors:
        if is_safe(current, color, assignment, graph):
            assignment[current] = color
            result = map_coloring(graph, colors, assignment, node + 1, nodes)
            if result:
                return result
            del assignment[current]
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
colors = ['Red', 'Green', 'Blue']

solution = map_coloring(graph, colors)
print("Color Assignment:", solution)
