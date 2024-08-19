import matplotlib.pyplot as plt
import networkx as nx

class NeuralNetworkVisualizer:
    def __init__(self, neural_net):
        self.neural_net = neural_net

    def draw(self):
        G = nx.DiGraph()
        pos = {}  # For storing the positions of the nodes

        # Layer-wise offset for vertical spacing
        layer_offsets = [len(layer.nodes) for layer in self.neural_net.layers]
        max_layer_size = max(layer_offsets)
        
        y_offset = 1  # Vertical offset between layers
        x_offset = 1  # Horizontal offset between nodes

        for i, layer in enumerate(self.neural_net.layers):
            layer_size = len(layer.nodes)
            for j, node in enumerate(layer.nodes):
                node_id = f"{node.type}_{i}_{j}"
                G.add_node(node_id)
                # Calculate the position: center the layer nodes horizontally
                pos[node_id] = (x_offset * i, y_offset * (max_layer_size - layer_size) / 2 + j * y_offset)

                # Add edges to the next layer nodes
                for conn in node.connections:
                    next_node_id = f"{conn.connected_to.type}_{i+1}_{self.neural_net.layers[i+1].nodes.index(conn.connected_to)}"
                    G.add_edge(node_id, next_node_id, weight=conn.weight)

        # Draw the graph
        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")

        # Draw edge labels (weights)
        edge_labels = {(u, v): f'{d["weight"]:.2f}' for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")

        plt.title("Neural Network Visualization")
        plt.show()





