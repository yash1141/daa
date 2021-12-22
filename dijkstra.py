import sys


def printSolution(dist):
    print("Vertex Distance from Source")
    for node in range(1,V):
        print("Distance of ", node, "is", dist[node])


def mindist(dist, sptSet):
    min = sys.maxsize
    for v in range(V):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v
    return min_index


def dijkstra(src):
    dist = [sys.maxsize] * V
    dist[src] = 0
    sptSet = [False] * V

    for _ in range(V):
        u = mindist(dist, sptSet)
        sptSet[u] = True
        for v in range(V):
            if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
    printSolution(dist)


V = 5
graph = [[0, 10, 0, 30, 100],
         [10, 0, 50, 0, 0],
         [0, 50, 0, 20, 10],
         [30, 0, 20, 0, 60],
         [100, 0, 10, 60, 0]
         ]

dijkstra(0)
