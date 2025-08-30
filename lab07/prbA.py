import sys, heapq
input = sys.stdin.readline

n, m, s, d = map(int, input().split())

def graph(n, m):
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    w = list(map(int, input().split()))
    g = {i:[] for i in range(1, n+1)}
    for i in range(m):
        g[u[i]].append((v[i], w[i]))
    return g
g = graph(n, m)

def dijkstra(g, n, s, d):
    dist = [float('inf') for _ in range(n+1)]
    parent = [None for _ in range(n+1)]

    dist[s] = 0
    pq = [(dist[s], s)]

    while pq:
        d_u, u = heapq.heappop(pq)
        if u == d: break
        if d_u == dist[u]:
            for v, w in g[u]:
                if dist[v] > d_u+w:
                    dist[v] = d_u+w
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v))
    
    if dist[d] == float('inf'):
        print(-1); exit()
    
    path = []
    curr = d
    while curr:
        path.append(curr)
        curr = parent[curr]

    print(dist[d])
    path.reverse()
    print(*path)
dijkstra(g, n, s, d)
