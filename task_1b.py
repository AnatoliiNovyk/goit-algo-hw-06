# Аналіз характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин (міст): {num_nodes}")
print(f"Кількість ребер (шляхів): {num_edges}")
print("\nСтупені вершин (кількість зв'язків для кожного міста):")
for city, degree in degrees.items():
    print(f"- {city}: {degree}")
