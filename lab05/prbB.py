import sys
sys.setrecursionlimit(2*100000+10)
input = sys.stdin.readline

def graph(ver, e):
    g = [[] for _ in range(ver+1)]
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    for i in range(e):
        g[u[i]].append(v[i])
        g[v[i]].append(u[i])

    return g

def dfs(g, s, visited, order):
    visited[s] = 1
    order.append(s)
    for v in g[s]:
        if visited[v]==0:
            dfs(g, v, visited, order)
    

n, m = map(int, input().split())
graphh = graph(n, m)

visited = [0]*(n+1)
order = []
dfs(graphh, 1, visited, order)

print(*order)