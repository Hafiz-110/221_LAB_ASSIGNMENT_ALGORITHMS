import sys
input = sys.stdin.readline

def graph(n):
    g = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        g[u].append(v); g[v].append(u)
    return g

n = int(input())
g = graph(n)

from collections import deque

def bfs(start):
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

A, _ = bfs(1)
B, dist_from_A = bfs(A)
diameter_length = dist_from_A[B]

print(diameter_length)
print(A, B)
