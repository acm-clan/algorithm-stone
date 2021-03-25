from manimlib import *

sys.path.append(os.getcwd() + '\\..\\')
from algomanim.algoscene import AlgoScene
from algomanim.algograph import AlgoGraph

class AlgoGraphScene(AlgoScene):
    def preconfig(self, settings):
        settings['node_size'] = 0.5
        settings['node_shape'] = 'circle'
        settings['highlight_color'] = "#e74c3c" # red

    def algo(self):
        graph = { 'A' : [ 'B', 'C', 'F', 'G' ], \
                  'B' : [ 'A', 'C', 'D', 'G' ], \
                  'C' : [ 'A', 'B', 'G' ], \
                  'D' : [ 'B', 'G' ], \
                  'E' : [ ], \
                  'F' : [ 'A', 'G' ], \
                  'G' : [ 'A', 'B', 'C', 'D', 'F' ] }

        algograph = AlgoGraph(self, graph, animated=True)
        algograph.show()

class AlgoGraphSceneSimple(AlgoScene):
    def preconfig(self, settings):
        settings['node_size'] = 0.5
        settings['node_shape'] = 'circle'
        settings['highlight_color'] = "#e74c3c" # red

    def algo(self):
        graph = { 'A' : [ 'B', 'C' ], \
                  'B' : [ 'A', 'C' ], \
                  'C' : [ 'A', 'B' ]}

        algograph = AlgoGraph(self, graph, animated=True)
        algograph.show()

class AlgoWeightedGraphSceneSimple(AlgoScene):
    def preconfig(self, settings):
        settings['node_size'] = 0.5
        settings['node_shape'] = 'circle'
        settings['highlight_color'] = "#e74c3c" # red

    def algo(self):
        graph = { 'A' : [ ('B', 1), ('C', 2) ], \
                  'B' : [ ('A', 1), ('C', 3) ], \
                  'C' : [ ('A', 2), ('B', 3) ]}

        algograph = AlgoGraph(self, graph, animated=True)
        algograph.show()
