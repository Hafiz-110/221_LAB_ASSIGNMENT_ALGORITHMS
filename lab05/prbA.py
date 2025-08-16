from collections import deque
import sys
input = sys.stdin.readline

def graph(v, e):
    graph = [[] for _ in range(v+1)]    # 1-indexed
    for i in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  # undirected
    
    return graph

def bfs(g, s):
    n = len(g)-1    # 1-indexed
    visited = [0]*(n+1)
    parent = [-1]*(n+1)
    distance = [-1]*(n+1)

    q = deque()
    visited[s] = 1
    distance[s] = 0
    q.append(s)
    order = []

    while q:
        u = q.popleft()
        order.append(u)
        for adj_v in graph[u]:
            if visited[adj_v]==0:
                visited[adj_v] = 1
                parent[adj_v] = u
                distance[adj_v] = distance[u]+1
                q.append(adj_v)
    print(*order)

n, m = map(int, input().split())    # vertices, edges
graph = graph(n, m)
bfs(graph, 1)
