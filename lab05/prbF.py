import sys
sys.setrecursionlimit(2*10**5+10)
input = sys.stdin.readline

def graph(ver, e):
    g = [[] for _ in range(ver+1)]
    for i in range(e):
        u, v = map(int, input().split())
        g[u].append(v)
    return g

# 0 = unvisited, 1 = visiting, 2 = visited
def dfs_cycle(g, s, visited):
    visited[s] = 1
    for v in g[s]:
        if visited[v] == 0:
            if dfs_cycle(g, v,  visited):
                return True
        elif visited[v] == 1:
            return True
    visited[s] = 2
    return False

n, m = map(int, input().split())
g = graph(n, m)

visited = [0]*(n+1); cycle = False
for i in range(1, n+1):
    if visited[i] == 0:
        if dfs_cycle(g, i, visited):
            cycle = True; break
        
if cycle: print('YES')
else: print('NO')

