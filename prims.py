import sys

def printMST(parent):
    print("Edge \tWeight")
    for i in range(1, V):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])


def mindist(dist, sptSet):
    min = sys.maxsize
    for v in range(V):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v
    return min_index


def primMST():
    dist = [sys.maxsize] * V
    dist[0] = 0
    sptSet = [False] * V
    parent = [None] * V
    parent[0] = -1
    for _ in range(V):
        u = mindist(dist, sptSet)
        sptSet[u] = True
        for v in range(V):
            if graph[u][v] > 0 and sptSet[v] == False and dist[v] > graph[u][v]:
                dist[v] = graph[u][v]
                parent[v] = u
    printMST(parent)


V = 5
graph = [[0, 2, 0, 6, 0],
         [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]
primMST()
