import sys, heapq
input = sys.stdin.readline

n, m, s, d = map(int, input().split())
w = [0] + list(map(int, input().split()))   # 1 indexed
def graph(n, m):
    g = {i:[] for i in range(1, n+1)}
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
    return g
g = graph(n, m)

def dijkstra(g, n, s, d, w):
    dist = [float('inf') for _ in range(n+1)]
    
    dist[s] = w[s]
    pq = [(dist[s], s)]

    while pq:
        curr_d, curr = heapq.heappop(pq)
        if curr_d == dist[curr]:
            for v in g[curr]:
                if dist[v] > dist[curr]+w[v]:
                    dist[v] = dist[curr]+w[v]
                    heapq.heappush(pq, (dist[v], v))
    
    return -1 if dist[d] == float('inf') else dist[d]
print(dijkstra(g, n, s, d, w))
