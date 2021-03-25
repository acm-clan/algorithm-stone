from manimlib import *
from algomanim.algoscene import AlgoScene
from algomanim.algograph import AlgoGraph

class AlgoDijkstras(AlgoScene):
    def preconfig(self, settings):
        settings['node_size'] = 0.5
        settings['node_shape'] = 'circle'
        settings['highlight_color'] = "#e74c3c" # red

    def algo(self):
        # graph = { 'A' : [ ('B', 1), ('C', 2) ],
        #           'B' : [ ('A', 1), ('C', 3) ],
        #           'C' : [ ('A', 2), ('B', 3) ]}

        graph = { 'A' : [ ('B', 1), ('G', 50) ], \
                  'B' : [ ('A', 1), ('C', 1), ('G', 8) ], \
                  'C' : [ ('B', 1), ('G', 2) ], \
                  'D' : [ ('G', 5) ], \
                  'E' : [ ], \
                  'F' : [ ('G', 6) ], \
                  'G' : [ ('A', 50), ('B', 2), ('C', 8), ('D', 5), ('F', 6) ] }


        algograph = AlgoGraph(self, graph, animated=False)
        algograph.show(animated=False)

        def dijsktra(self, graph, initial):
            dist = {}
            prev = {}
            queue = []

            for vertex in graph.graph:
                dist[vertex] = float('inf')
                prev[vertex] = None
                queue.append(vertex)

            dist[initial] = 0
            queue.sort(key=lambda v: dist[v])
            while queue:
                min_vertex = queue.pop(0)
                min_vertex_node = graph.get_node(min_vertex)

                self.insert_pin("min_vertex", min_vertex_node)

                for edge, weight in min_vertex_node.adjs:
                    if edge not in queue:
                        continue

                    edge_node = graph.get_node(edge)
                    self.insert_pin("check_edge", min_vertex_node, edge_node)
                    alt = dist[min_vertex] + weight

                    if alt < dist[edge]:
                        if prev[edge]:
                            self.insert_pin("prv_edge", graph.get_node(prev[edge]), edge_node)
                        self.insert_pin("min_edge", min_vertex_node, edge_node)
                        dist[edge] = alt
                        prev[edge] = min_vertex
                        queue.sort(key=lambda edge: dist[edge])
                    else:
                        self.insert_pin("check_edge_done", min_vertex_node, edge_node)

                self.insert_pin("min_vertex_done", min_vertex_node)
            return dist, prev

        dist, _ = dijsktra(self, algograph, 'A')
        print(dist)

    def customize(self):
        self.chain_pin_highlight("min_vertex")
        self.chain_pin_highlight("min_vertex_done", '#66e0ff', dehighlight=False)
        self.chain_pin_highlight_line("check_edge")
        self.chain_pin_highlight_line("min_edge", '#66e0ff', dehighlight=False)

        self.chain_pin_dehighlight_line("check_edge_done")
        self.chain_pin_dehighlight_line("prv_edge")
