import sys
input = sys.stdin.readline

def graph(ver, e):
    g = [[] for _ in range(ver+1)]
    i_deg = [0 for _ in range(ver+1)]
    for _ in range(e):
        u, v = map(int, input().split())
        g[u].append(v)
        i_deg[v] += 1
    return g, i_deg

n, m = map(int, input().split())
g, i_degree = graph(n, m)


from collections import deque

def topo_sort(g, i_deg, n):
    res = []
    q = deque()
    for i in range(1, n+1):  # 1 to n since vertex can be from 1 to n
        if i_deg[i]==0:
            q.append(i)

    while q:
        u = q.popleft()
        res.append(u)
        for v in g[u]:
            i_deg[v] -= 1
            if i_deg[v] == 0: q.append(v)

    if len(res) == n: print(*res)
    else: print(-1)

topo_sort(g, i_degree, n)
