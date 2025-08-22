import sys
from collections import deque
input = sys.stdin.readline

def graph(n, m):
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    return g

def bfs(g, sources, n):
    dist = [-1] * (n + 1)
    dq = deque()
    for s in sources:
        if dist[s] == -1:
            dist[s] = 0
            dq.append(s)

    while dq:
        u = dq.popleft()
        for v in g[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                dq.append(v)
    return dist

n, m, s, q = map(int, input().split())
g = graph(n, m)
sources = list(map(int, input().split()))
dests = list(map(int, input().split()))

dist = bfs(g, sources, n)

results = []
for d in dests:
    results.append(str(dist[d]))

print(" ".join(results))
