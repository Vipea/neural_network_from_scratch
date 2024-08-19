import random

class Node:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.connections = []
        self.bias = random.uniform(0,1)