import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
def graph(n, m):
    g = {i:[] for i in range(1, n+1)}
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))
    return g
g = graph(n, m)

def dijkstra(g, n):
    inf = float('inf')
    danger = [inf for _ in range(n+1)]

    danger[1] = 0
    pq = [(danger[1], 1)]

    while pq:
        du, u = heapq.heappop(pq)
        if du == danger[u]:
            for v, w in g[u]:
                if danger[v] > max(du, w):
                    danger[v] = max(du, w)
                    heapq.heappush(pq, (danger[v], v))
    
    print(*(-1 if i==inf else i for i in danger[1:]))

dijkstra(g, n)
