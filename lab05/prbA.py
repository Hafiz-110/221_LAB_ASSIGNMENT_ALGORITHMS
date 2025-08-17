from collections import deque
import sys
input = sys.stdin.readline

def graph(ver, e):
    g = [[] for _ in range(ver+1)]
    for _ in range(e):
        u, v = map(int, input().split())
        g[u].append(v); g[v].append(u)
    return g

def bfs(g ,s):
    n = len(g)-1
    visited = {i:0 for i in range(1, n+1)}
    parent = {i:-1 for i in range(1, n+1)}
    distance = {i:-1 for i in range(1, n+1)}
    order = []

    visited[s] = 1; distance[s] = 0
    q = deque(); q.append(s)

    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            if visited[v] == 0:
                visited[v] = 1
                parent[v] = u
                distance[v] = distance[u] + 1
                q.append(v)
    print(*order)

n, m = map(int, input().split())
g = graph(n, m)
bfs(g, 1)
