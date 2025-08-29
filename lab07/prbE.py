import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
def graph(n, m):
    g = {i:[] for i in range(1, n+1)}
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    w = list(map(int, input().split()))
    for i in range(m):
        g[u[i]].append((v[i], w[i]))
    return g
g = graph(n, m)

def dijsktra_parity(g, n):
    inf, even, odd = float('inf'), 0, 1
    dist = [[inf, inf] for _ in range(n+1)]
    
    dist[1][even] = 0; dist[1][odd] = 0
    pq = [(0, 1, even), (0, 1, odd)]

    while pq:
        d_u, u, p = heapq.heappop(pq)
        if d_u == dist[u][p]:
            for v, w in g[u]:
                wp = w%2
                if wp != p and dist[v][wp] > dist[u][p]+w:
                    dist[v][wp] = dist[u][p]+w
                    heapq.heappush(pq, (dist[v][wp], v, wp))
    
    ans = min(dist[n][even], dist[n][odd])
    return -1 if ans == inf else ans

print(dijsktra_parity(g, n))
