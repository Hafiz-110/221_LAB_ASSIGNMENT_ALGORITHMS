import sys
from collections import deque
input = sys.stdin.readline

def graph(n):
    g = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    return g

def bfs(start, g, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    
    while q:
        u = q.popleft()
        for v in g[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    
    farthest_node = dist.index(max(dist))
    return farthest_node, dist

n = int(input())
g = graph(n)

A, _ = bfs(1, g, n)
B, dist_from_A = bfs(A, g, n)
diameter_length = dist_from_A[B]

print(diameter_length)
print(A, B)
