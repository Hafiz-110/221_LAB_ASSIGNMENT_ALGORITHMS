import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
def graphw_weight(n, m):
    g = {i:[] for i in range(1, n+1)}
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))
    return g
g = graphw_weight(n, m)

def dijkstra(g, n):
    danger = [float('inf') for _ in range(n+1)]
    
    danger[1] = 0
    pq = [(danger[1], 1)]
    while pq:
        curr_d, curr = heapq.heappop(pq)
        if curr_d == danger[curr]:
            for v, w in g[curr]:
                if danger[v] > max(danger[curr], w):
                    danger[v] = max(danger[curr], w)
                    heapq.heappush(pq, (danger[v], v))
    
    for i in danger[1:]:
        print(i if i != float('inf') else -1, end=' ')

dijkstra(g, n)
