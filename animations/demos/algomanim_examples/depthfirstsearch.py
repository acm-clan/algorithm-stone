from algomanim.algoscene import AlgoScene
from algomanim.algograph import AlgoGraph

class DepthFirstSearch(AlgoScene):
    def preconfig(self, settings):
        settings['node_size'] = 0.5
        settings['node_shape'] = 'circle'
        settings['highlight_color'] = "#e74c3c" # red

    def algo(self):
        graph = { 'A' : [ 'B', 'C', 'F', 'G' ],
                  'B' : [ 'A', 'C', 'D', 'G' ],
                  'C' : [ 'A', 'B', 'G' ],
                  'D' : [ 'B', 'G' ],
                  'E' : [ ],
                  'F' : [ 'A', 'G' ],
                  'G' : [ 'A', 'B', 'C', 'D', 'F' ] }

        algograph = AlgoGraph(self, graph, show=True, animated=False)

        def dfs_helper(node, visited):
            visited.append(node.val)
            for neighbor_id, _ in node.adjs:
                if neighbor_id not in visited:
                    neighbor_node = node.visit(neighbor_id)
                    dfs_helper(neighbor_node, visited)
                    node.leave(neighbor_id)

        curr_node = algograph.select_node('A')

        dfs_helper(curr_node, [])
