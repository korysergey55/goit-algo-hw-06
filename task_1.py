import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
stations = ["Депо", "Вишнева", "Яковенка", "Центральна", "Березка", "Гайок"]
G.add_nodes_from(stations)


edges = [
    ("Депо", "Вишнева"),
    ("Вишнева", "Яковенка"),
    ("Яковенка", "Центральна"),
    ("Центральна", "Березка"),
    ("Березка", "Гайок"),
    ("Гайок", "Депо"),
    ("Депо", "Центральна"),
]


G.add_edges_from(edges)
pos = nx.circular_layout(G)


edge_labels = {
    ("Депо", "Вишнева"): "1",
    ("Вишнева", "Яковенка"): "2",
    ("Яковенка", "Центральна"): "3",
    ("Центральна", "Березка"): "4",
    ("Березка", "Гайок"): "5",
    ("Гайок", "Депо"): "6",
    ("Депо", "Центральна"): "7",
}


nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="yellow",
    node_size=2000,
    edge_color="blue",
    font_size=15,
    font_color="darkgreen",
)


nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_color="red",
    font_size=12,
)

plt.title("Схема руху дитячої залізниці в Києві з нумерацією ребер")
plt.show()


num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_centrality = nx.degree_centrality(G)


print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degree_centrality.items():
    print(f"{node}: {degree:.2f}")
