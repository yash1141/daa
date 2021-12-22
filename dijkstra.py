import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = None

    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print(node, "t", dist[node])

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index
    
    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist)

g = Graph(5)
g.graph = [[0, 10, 0, 30, 100],
           [10, 0, 50, 0, 0],
           [0, 50, 0, 20, 10],
           [30, 0, 20, 0, 60],
           [100, 0, 10, 60, 0]
           ]

g.dijkstra(0)
