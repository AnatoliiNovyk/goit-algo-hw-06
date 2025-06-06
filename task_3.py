# Додавання ваг до ребер (відстані в км)
weighted_edges = [
    ("Київ", "Вінниця", {'weight': 267}), ("Київ", "Черкаси", {'weight': 190}), ("Київ", "Полтава", {'weight': 342}),
    ("Вінниця", "Львів", {'weight': 365}), ("Вінниця", "Одеса", {'weight': 442}),
    ("Одеса", "Черкаси", {'weight': 447}), ("Одеса", "Кривий Ріг", {'weight': 294}),
    ("Черкаси", "Полтава", {'weight': 270}), ("Черкаси", "Дніпро", {'weight': 272}),
    ("Полтава", "Харків", {'weight': 143}), ("Полтава", "Дніпро", {'weight': 195}),
    ("Дніпро", "Харків", {'weight': 218}), ("Дніпро", "Запоріжжя", {'weight': 82}), ("Дніпро", "Кривий Ріг", {'weight': 150}),
    ("Запоріжжя", "Кривий Ріг", {'weight': 165})
]

# Створення нового графа з вагами
G_weighted = nx.Graph()
G_weighted.add_nodes_from(cities)
G_weighted.add_edges_from(weighted_edges)

# Пошук найкоротших шляхів від Львова до всіх інших міст за допомогою алгоритму Дейкстри
start_city = "Львів"
shortest_paths = nx.single_source_dijkstra_path(G_weighted, source=start_city)
shortest_path_lengths = nx.single_source_dijkstra_path_length(G_weighted, source=start_city)

print(f"Найкоротші шляхи від міста {start_city}:\n")
for city, path in shortest_paths.items():
    length = shortest_path_lengths[city]
    print(f"До міста {city}:")
    print(f"  - Шлях: {' -> '.join(path)}")
    print(f"  - Відстань: {length} км\n")

# Візуалізація зваженого графа
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G_weighted, seed=42)
labels = nx.get_edge_attributes(G_weighted, 'weight')
nx.draw(G_weighted, pos, with_labels=True, node_size=2500, node_color='lightgreen', font_size=12, font_weight='bold')
nx.draw_networkx_edge_labels(G_weighted, pos, edge_labels=labels)
plt.title("Зважена транспортна мережа міст України (відстані в км)")
plt.show()
