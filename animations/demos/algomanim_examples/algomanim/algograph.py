import numpy as np
from manimlib import *
from algomanim.algonode import AlgoNode
from algomanim.metadata import attach_metadata

class AlgoGraph:
    def __init__(self, scene, graph, show=False, animated=False):
        self.scene = scene
        self.graph = self.dic_to_algograph(graph)
        if show:
            self.show(animated=animated)

    def dic_to_algograph(self, graph):
        algograph = {}
        for key in graph:
            new_adj = []
            # Makes it work if graph doesn't have weights
            for adj in graph[key]:
                if not isinstance(adj, tuple):
                    new_adj.append((adj, None))
            if not new_adj:
                new_adj = graph[key]

            algograph[key] = AlgoGraphNode(self.scene, algograph, key, new_adj)
        return algograph

    @attach_metadata
    def show(self, metadata=None, animated=True):
        self.arrange_nodes()
        self.show_nodes(metadata, animated)
        self.show_lines(metadata, animated=animated)


    def get_node(self, key):
        return self.graph[key]

    @attach_metadata
    def select_node(self, node_id, metadata=None, animated=True, w_prev=False):
        node = self.graph[node_id]
        node.highlight(metadata=metadata, animated=animated, w_prev=w_prev)
        return node

    def arrange_nodes(self):
        if AlgoGraphNode.n_id > 0:
            angle = 2 * np.pi / (AlgoGraphNode.n_id)

            for key in self.graph:
                node = self.graph[key]
                new_angle = angle*node.n_id
                node.grp.move_to(3*np.array([np.cos(new_angle), np.sin(new_angle), 0]))

    def show_nodes(self, metadata=None, animated=True, w_prev=False):
        for node_key in self.graph:
            self.graph[node_key].show(metadata=metadata, animated=animated, w_prev=w_prev)
            if not w_prev:
                w_prev = True

    def show_lines(self, metadata=None, animated=True, w_prev = False):
        lines_done = {}
        for node_key in self.graph:
            self.graph[node_key].show_lines(lines_done, metadata, animated=animated, w_prev=w_prev)
            if not w_prev:
                w_prev = True


class AlgoGraphNode(AlgoNode):
    n_id = 0
    def __init__(self, scene, graph, val, adjs):
        self.graph = graph
        self.adjs = adjs
        self.n_id = AlgoGraphNode.n_id
        AlgoGraphNode.n_id += 1
        super().__init__(scene, val)

    @attach_metadata
    def visit(self, neighbour_id, metadata=None, animated=True, w_prev=False):
        node = self.graph[neighbour_id]
        node.highlight(metadata=metadata, animated=animated, w_prev=w_prev)
        node.highlight_line(self, metadata=metadata, animated=animated, w_prev=True)
        return node

    @attach_metadata
    def leave(self, neighbour_id, metadata=None, animated=True, w_prev=False):
        node = self.graph[neighbour_id]
        node.dehighlight(metadata=metadata, animated=animated, w_prev=w_prev)
        node.dehighlight_line(self, metadata=metadata, animated=animated, w_prev=True)
        return node

    def show_lines(self, lines_done, metadata=None, animated=True, w_prev=False):
        if self.adjs is not None:
            for target, weight in self.adjs:
                if target not in lines_done or self.val not in lines_done[target]:
                    if target not in lines_done:
                        lines_done[target] = [self.val]
                    elif self.val not in lines_done[target]:
                        lines_done[target].append(self.val)
                    if self.val not in lines_done:
                        lines_done[self.val] = [target]
                    elif target not in lines_done[self.val]:
                        lines_done[self.val].append(target)

                    self.add_line(self.graph[target], weight, metadata=metadata,
                                                animated=animated, w_prev=w_prev)
