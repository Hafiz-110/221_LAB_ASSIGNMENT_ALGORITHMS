import sys, heapq
input = sys.stdin.readline

test = int(input())
for i in range(test):
    n, m, s, d = map(int, input().split())
    w = [0] + list(map(int, input().split()))
    def graph(n, m):
        g = {i:[] for i in range(1, n+1)}
        for _ in range(m):
            u, v = map(int, input().split())
            g[u].append(v)
        return g
    g = graph(n, m)
    

    def dijkstra(g, n, s, d):
        inf = float('inf')
        dist = [inf for _ in range(n+1)]
        
        dist[s] = 0
        pq = [(dist[s], s)]

        while pq:
            du, u = heapq.heappop(pq)
            
            if du == dist[u]:
                for v in g[u]:
                    if dist[v] > w[u]+w[v]**2+du:
                        dist[v] = w[u]+w[v]**2+du
                        
                        heapq.heappush(pq, (dist[v], v))
        print(-1 if dist[d]==inf else dist[d])

    dijkstra(g, n, s, d)
