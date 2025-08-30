import sys, heapq
input = sys.stdin.readline

n, m, s, t = map(int, input().split())
def garph(n, m):
    g = {i:[] for i in range(1, n+1)}
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
    return g
g = garph(n, m)

def dijkstra(g, n, s):
    inf = float('inf')
    dist = [inf for _ in range(n+1)]

    dist[s] = 0
    pq = [(dist[s], s)]

    while pq:
        du, u = heapq.heappop(pq)
        if du == dist[u]:
            for v, w in g[u]:
                if dist[v] > du+w:
                    dist[v] = du+w
                    heapq.heappush(pq, (dist[v], v))
    return dist

dist_a = dijkstra(g, n, s)
dist_b = dijkstra(g, n, t)

inf = float('inf')
best_time = inf; best_n = -1
for i in range(1, n+1):
    if dist_a[i]!=inf and dist_b!=inf:
        meet_time = max(dist_a[i], dist_b[i])
        if meet_time<best_time or (meet_time==best_time and i<best_n):
            best_time = meet_time
            best_n = i

print(-1 if best_n==-1 else f'{best_time} {best_n}')
