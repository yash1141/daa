import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = None

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def mindist(self, dist, sptSet):
        min = sys.maxsize
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def primMST(self):
        dist = [sys.maxsize] * self.V
        parent = [None] * self.V
        dist[0] = 0 
        sptSet = [False] * self.V
        parent[0] = -1
        for _ in range(self.V):
            u = self.mindist(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > self.graph[u][v]:
                    dist[v] = self.graph[u][v]
                    parent[v] = u
        self.printMST(parent)

g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]
g.primMST()
