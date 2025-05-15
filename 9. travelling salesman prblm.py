from itertools import permutations

def tsp(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    min_path = float('inf')
    for perm in permutations(vertices):
        path_cost = graph[start][perm[0]]
        for i in range(len(perm) - 1):
            path_cost += graph[perm[i]][perm[i+1]]
        path_cost += graph[perm[-1]][start]
        min_path = min(min_path, path_cost)
    return min_path

graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}
print("Minimum Cost:", tsp(graph, 'A'))
