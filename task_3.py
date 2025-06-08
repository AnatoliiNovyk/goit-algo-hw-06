import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra_manual(graph_dict, start_node):
    """
    Реалізація алгоритму Дейкстри для пошуку найкоротших шляхів.
    """
    distances = {node: float('infinity') for node in graph_dict}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, edge_data in graph_dict[current_node].items():
            weight = edge_data.get('weight', 1)
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

# --- Основна частина програми для Завдання 3 ---

# 1. Створення графа (який був розроблений у Завданні 1)
G = nx.Graph()
cities = ["Київ", "Львів", "Одеса", "Харків", "Дніпро", "Вінниця", "Ужгород", "Чернівці", "Херсон", "Запоріжжя"]
G.add_nodes_from(cities)

# 2. Додавання ребер з РЕАЛЬНИМИ вагами (приблизні відстані в км)
print("Додавання реальних ваг до ребер графа (відстані в км)...")
real_distances = [
    ("Київ", "Львів", 540), ("Київ", "Харків", 480), ("Київ", "Одеса", 475), 
    ("Київ", "Дніпро", 477), ("Київ", "Вінниця", 270),
    ("Львів", "Вінниця", 360), ("Львів", "Ужгород", 270), ("Львів", "Чернівці", 280),
    ("Одеса", "Дніпро", 450), ("Одеса", "Херсон", 200),
    ("Харків", "Дніпро", 220), ("Харків", "Запоріжжя", 300),
    ("Дніпро", "Запоріжжя", 85), ("Дніпро", "Херсон", 325),
    ("Вінниця", "Чернівці", 285)
]
G.add_weighted_edges_from(real_distances)

# 3. Виконання алгоритму Дейкстри
print("\n--- Результати роботи алгоритму Дейкстри для всіх вершин ---")
graph_as_dict = nx.to_dict_of_dicts(G)

for start_node in G.nodes():
    shortest_distances = dijkstra_manual(graph_as_dict, start_node)
    print(f"\nНайкоротші шляхи від '{start_node}':")
    for node, distance in sorted(shortest_distances.items()):
        print(f"  - до '{node}': {distance} км")

# 4. Візуалізація фінального зваженого графа
print("\nВізуалізація зваженого графа з реальними відстанями...")
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(12, 10))
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2500, font_size=10, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.title("Завдання 3: Модель транспортної мережі України (з реальними відстанями)")
plt.show()
