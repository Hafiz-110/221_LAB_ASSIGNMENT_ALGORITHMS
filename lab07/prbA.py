import sys, heapq
input = sys.stdin.readline


n, m, s, d = map(int, input().split())

def graphw_weight(n, m):
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    w = list(map(int, input().split()))
    g = {i:[] for i in range(1, n+1)}
    for i in range(m):
        g[u[i]].append((v[i], w[i]))
    return g

g = graphw_weight(n, m)

def dijkstra(g, n, s, d):
    dist = [float('inf') for _ in range(n+1)]
    p = [None for _ in range(n+1)]

    dist[s] = 0
    pq = [(0, s)]

    while pq:
        dist_u, u = heapq.heappop(pq)
        if u==d: break 

        if dist_u == dist[u]:
            for v, w in g[u]:
                if dist[u]+w < dist[v]:
                    dist[v] = dist[u]+w
                    p[v] = u
                    heapq.heappush(pq, (dist[v], v))    # dijkstra algo done!

    # path construction
    if dist[d] == float('inf'): return -1, []

    path = []
    curnt = d
    while curnt:
        path.append(curnt)
        curnt = p[curnt]
    path.reverse()
    return dist[d], path

des_d, path = dijkstra(g, n, s, d)

if des_d == -1: print(-1)
else:
    print(des_d)
    print(*path)
