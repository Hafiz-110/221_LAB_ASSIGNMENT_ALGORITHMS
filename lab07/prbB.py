import sys, heapq
input = sys.stdin.readline

n, m, s, t = map(int, input().split())
def graphw_weight(n, m):
    g = {i:[] for i in range(1, n+1)}
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))

    return g
g = graphw_weight(n, m)

def dijkstra(g, s, n):
    dist = [float('inf') for _ in range(n+1)]
    

    dist[s] = 0
    pq = [(0, s)]
    
    while pq:
        curr_d, curr = heapq.heappop(pq)
        if curr_d == dist[curr]:
            for v, w in g[curr]:
                if dist[curr]+w < dist[v]:
                    dist[v] = dist[curr]+w
                    
                    heapq.heappush(pq, (dist[v], v))
    return dist

dist_s = dijkstra(g, s, n)
dist_t = dijkstra(g, t, n)

best_time = float('inf'); best_n = -1
for i in range(1, n+1):
    if dist_s[i]!=float('inf') and dist_t[i]!=float('inf'):
        meet_time = max(dist_s[i], dist_t[i])
        if meet_time<best_time or (meet_time==best_time and i<best_n):
            best_time = meet_time
            best_n = i
if best_n == -1: print(-1)
else: print(best_time, best_n)

