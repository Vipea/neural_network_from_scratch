from node import Node
from layer import Layer
from neuralnet import NeuralNet
from visualizer import NeuralNetworkVisualizer

x0 = Node(type="input", value = 0.7)
x1 = Node(type="input", value = 0.3)

h0 = Node(type="hidden", value = 0)
h1 = Node(type="hidden", value = 0)

y0 = Node(type="output", value = 0)

layer0 = Layer(position=0, nodes=[x0, x1])
layer1 = Layer(position=0, nodes=[h0, h1])
layer2 = Layer(position=0, nodes=[y0])

neuralnet = NeuralNet(layers=[layer0, layer1, layer2])

neuralnet.initialise_connections()
visualizer = NeuralNetworkVisualizer(neuralnet)
visualizer.draw()

neuralnet.forward_pass()
visualizer = NeuralNetworkVisualizer(neuralnet)
visualizer.draw()