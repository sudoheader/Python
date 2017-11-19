from collections import namedtuple, deque
from pprint import pprint as pp


inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

class Graph():
    def __init__(self, edges):
        self.edges = edges2 = [Edge(*edge) for edge in edges]
        self.vertices = set(sum(([e.start, e.end] for e in edges2), []))

    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))
        #pp(neighbours)

        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:                                  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        #pp(previous)
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s


graph = Graph([("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
               ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
               ("e", "f", 9)])

graph1 = Graph([("a", "b", 7), ("a", "c", 3), ("a", "d", 1), ("b", "e", 2),
                ("c", "b", 1), ("d", "a", 2), ("d", "c", 6), ("e", "c", 2)])

graph2 = Graph([("a", "b", 7), ("a", "c", 3), ("b", "e", 2), ("c", "b", 1),
                ("d", "a", 2), ("d", "c", 6), ("e", "c", 2)])

graph3 = Graph([("a", "b", 2), ("a", "e", -1), ("b", "c", -2), ("c", "e", 1),
                ("d", "a", 1), ("d", "c", 2), ("e", "b", 2), ("e", "d", 3)])

pp(graph.dijkstra("a", "e"))

# Graph 1 with source = d
pp(graph1.dijkstra("d", "a"))
pp(graph1.dijkstra("d", "b"))
pp(graph1.dijkstra("d", "c"))
pp(graph1.dijkstra("d", "e"))

# Graph 2 with source = a
pp(graph2.dijkstra("a", "b"))
pp(graph2.dijkstra("a", "c"))
pp(graph2.dijkstra("a", "d"))
pp(graph2.dijkstra("a", "e"))

# Graph 3 with source = a
pp(graph2.dijkstra("a", "b"))
pp(graph2.dijkstra("a", "c"))
pp(graph2.dijkstra("a", "d"))
pp(graph2.dijkstra("a", "e"))

# Graph 3 with source = e
pp(graph2.dijkstra("e", "a"))
pp(graph2.dijkstra("e", "b"))
pp(graph2.dijkstra("e", "c"))
pp(graph2.dijkstra("e", "d"))
