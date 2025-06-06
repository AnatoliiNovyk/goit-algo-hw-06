# Реалізація DFS для пошуку шляху
def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    visited = {start}
    while stack:
        (vertex, path) = stack.pop()
        for neighbor in set(graph.neighbors(vertex)) - visited:
            if neighbor == goal:
                return path + [neighbor]
            visited.add(neighbor)
            stack.append((neighbor, path + [neighbor]))

# Реалізація BFS для пошуку шляху
def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    visited = {start}
    while queue:
        (vertex, path) = queue.pop(0)
        for neighbor in set(graph.neighbors(vertex)) - visited:
            if neighbor == goal:
                return path + [neighbor]
            visited.add(neighbor)
            queue.append((neighbor, path + [neighbor]))

# Пошук шляхів між Львовом та Харковом
start_node = "Львів"
end_node = "Харків"

dfs_route = dfs_path(G, start_node, end_node)
bfs_route = bfs_path(G, start_node, end_node)

print(f"Шлях знайдений за допомогою DFS: {dfs_route}")
print(f"Шлях знайдений за допомогою BFS: {bfs_route}")
