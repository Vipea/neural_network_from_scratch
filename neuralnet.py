import random
from connection import Connection

class NeuralNet:
    def __init__(self, layers):
        self.layers = layers

    def initialise_connections(self):
        for layer_index in range(len(self.layers)-1):
            for start_node in self.layers[layer_index].nodes:
                for end_node in self.layers[layer_index+1].nodes:
                    start_node.connections.append(Connection(connected_to=end_node,
                                                             weight=random.uniform(0, 1)))
                    
    
