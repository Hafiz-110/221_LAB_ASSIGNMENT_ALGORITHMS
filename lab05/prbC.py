from collections import deque
import sys
input = sys.stdin.readline

def graph(ver, e):
    g = [[] for _ in range(ver+1)]
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    for i in range(e):
        g[u[i]].append(v[i])
        g[v[i]].append(u[i])
    
    for i in range(1, ver+1):
        g[i].sort()

    return g

n, m, s, d = map(int, input().split())
graphh = graph(n, m)

distance = {i:float('inf') for i in range(1, n+1)}
parent = {i:-1 for i in range(1, n+1)}
distance[s] = 0
parent[s] = None

q = deque(); q.append(s)

def bfs():
    while q:
        u = q.popleft()
        for v in graphh[u]:
            if distance[v] > distance[u]+1:
                distance[v] = distance[u]+1
                parent[v] = u
                q.append(v)
bfs()

# backtracking to source
if distance[d] == float('inf'): print(-1)
else:
    path = []
    u = d
    while u:
        path.append(u)
        u = parent[u]
    print(len(path) - 1)
    print(*reversed(path))
