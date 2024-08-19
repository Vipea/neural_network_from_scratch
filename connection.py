from node import Node

class Connection:
    def __init__(self, connected_to: Node, weight: float):
        self.connected_to = connected_to
        self.weight = weight

# !!! calculate weighted sum
# !!! squish weighed sum result to 0-1 with sigmoid
