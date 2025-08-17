from collections import deque
import sys
input = sys.stdin.readline

def graph(ver, e):
    g = [[] for _ in range(ver+1)]
    for i in range(e):
        u, v = map(int, input().split())
        g[u].append(v)

    return g

n, m, s, d, k = map(int, input().split())
graphh = graph(n, m)

def bfs(g, s, d, n):
    distance = {i:float('inf') for i in range(1, n+1)}
    parent = {i:-1 for i in range(1, n+1)}
    distance[s] = 0
    parent[s] = None
    q = deque(); q.append(s)
    while q:
        u = q.popleft()
        for v in g[u]:
            if distance[v] > distance[u]+1:
                distance[v] = distance[u]+1
                parent[v] = u
                q.append(v)

    if distance[d] == float('inf'): return -1, []

    path = []
    u = d
    while u:
        path.append(u)
        u = parent[u]
    path.reverse()
    return len(path)-1, path 

len_path1, path1 = bfs(graphh, s, k, n)
if len_path1 == -1:
    print(-1); exit()

len_path2, path2 = bfs(graphh, k, d, n)
if len_path2 == -1:
    print(-1); exit()

full_path = path1+path2[1:]
print(len(full_path)-1)
print(*full_path)



