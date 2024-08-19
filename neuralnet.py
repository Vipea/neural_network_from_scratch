import random
from connection import Connection

import math
class NeuralNet:
    def __init__(self, layers):
        self.layers = layers

    def initialise_connections(self):
        for layer_index in range(len(self.layers)-1):
            for start_node in self.layers[layer_index].nodes:
                for end_node in self.layers[layer_index+1].nodes:
                    start_node.connections.append(Connection(connected_to=end_node,
                                                             weight=random.uniform(0, 1)))
                    
    def forward_pass(self):
        for layer_index in range(len(self.layers)-1):
            for start_node in self.layers[layer_index].nodes:
                for connection in start_node.connections:
                    end_node = connection.connected_to
                    raw_value = start_node.value * connection.weight + end_node.bias

                    # Apply sigmoid
                    end_node.value = 1 / (1 + math.exp(-raw_value))
    