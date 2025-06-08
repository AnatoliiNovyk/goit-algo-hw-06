import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra_manual(graph_dict, start_node):
    """
    Реалізація алгоритму Дейкстри для пошуку найкоротших шляхів.

    Важливе зауваження: Ця реалізація призначена для графів з невід'ємними вагами ребер.
    Вона не буде коректно працювати, якщо у графі є ребра з негативними вагами.

    Аргументи:
        graph_dict (dict): Граф, представлений у вигляді словника суміжності.
        start_node (any): Вершина, з якої починається пошук.

    Повертає:
        tuple: Кортеж із двох словників: (distances, previous_nodes).
               - `distances`: Найкоротші відстані від start_node до всіх інших вершин.
               - `previous_nodes`: Словник для відновлення найкоротшого шляху.
    """
    # Перевірка на існування стартової вершини
    if start_node not in graph_dict:
        raise ValueError(f"Вершина {start_node} не знайдена у графі.")

    distances = {node: float('infinity') for node in graph_dict}
    distances[start_node] = 0
    previous_nodes = {node: None for node in graph_dict}
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, edge_data in graph_dict[current_node].items():
            weight = edge_data['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous_nodes

def reconstruct_path(previous_nodes, start_node, end_node):
    """
    Допоміжна функція для відновлення шляху зі словника previous_nodes.
    """
    path = []
    current_node = end_node
    while current_node is not None:
        path.insert(0, current_node)
        if current_node == start_node:
            break
        current_node = previous_nodes.get(current_node) # .get() для безпеки
    
    if path and path[0] == start_node:
        return path
    else:
        return None # Шлях не існує

# --- Основна частина програми ---

# 1. Створення графа та додавання реальних ваг
G = nx.Graph()
cities = ["Київ", "Львів", "Одеса", "Харків", "Дніпро", "Вінниця", "Ужгород", "Чернівці", "Херсон", "Запоріжжя"]
G.add_nodes_from(cities)
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

# 2. Виконання алгоритму
print("--- Результати роботи алгоритму Дейкстри ---")
graph_as_dict = nx.to_dict_of_dicts(G)

# Пошук шляхів від одного міста, наприклад, від Ужгорода
start_city = "Ужгород"
distances_from_start, prev_nodes_from_start = dijkstra_manual(graph_as_dict, start_city)

print(f"\nНайкоротші маршрути від міста '{start_city}':\n")
for city in sorted(cities):
    distance = distances_from_start.get(city, float('infinity'))
    path = reconstruct_path(prev_nodes_from_start, start_city, city)
    
    if path:
        print(f"  - Маршрут до '{city}': {' -> '.join(path)}")
        print(f"    Загальна відстань: {distance} км\n")
    else:
        print(f"  - Маршрут до '{city}': Шлях не знайдено\n")

# 3. Візуалізація
print("\nВізуалізація зваженого графа з реальними відстанями...")
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(12, 10))
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2500, font_size=10, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.title("Завдання 3: Модель транспортної мережі України (з реальними відстанями)")
plt.show()
