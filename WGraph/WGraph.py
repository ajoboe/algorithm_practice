
class WGraph:
    """An adjacency-list implementation of a weighted graph.
    """
    def get_n(self):
        """ return the number of vertices """
        pass

    def get_m(self):
        """ return the number of exges """
        return _m

    def get_edges(self):
        """ return a list of edges in the from u, v, weight """
        edges = []
        # how do we make sure we don't get duplicate edges?
        # always put the smaller vert first, then make the list a set
        for w in self._weights


    def __init__(self, num_verts, edge_list):
        pass

    def add_edge(self, u, v, weight):
        self._verts[u].append(v)
        self._weights[u][len(self._verts[u])-1] = weight
        self._m += 1
