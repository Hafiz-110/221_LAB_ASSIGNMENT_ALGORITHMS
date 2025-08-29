import sys, heapq
input = sys.stdin.readline

n, m, s, d = map(int, input().split())
def graph(n, m):
    g = {i: [] for i in range(1, n+1)}
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))
    return g
g = graph(n, m)

def dijkstra(g, n, s, des):
    inf = float('inf')
    first = [inf for _ in range(n+1)]
    second = [inf for _ in range(n+1)]
    
    first[s] = 0
    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)
        
        for v, w in g[u]:
            if first[v] > d+w:
                second[v] = first[v]
                first[v] = d+w
                heapq.heappush(pq, (first[v], v))
            elif first[v] < d+w < second[v]:
                second[v] = d+w
                heapq.heappush(pq, (second[v], v))
    
    return -1 if second[des] == inf else second[des]
print(dijkstra(g, n, s, d))
