import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def graph(ver, e):
    g = [[] for _ in range(ver+1)]
    for _ in range(e):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    return g

def dfs(u, parent, g, subtree_size):
    subtree_size[u] = 1  
    for v in g[u]:
        if v != parent:   
            dfs(v, u, g, subtree_size)
            subtree_size[u] += subtree_size[v]  

test = int(input())
for i in range(test):
    n, r = map(int, input().split())  
    graphh = graph(n, n-1)

    subtree_size = [0] * (n+1)

    dfs(r, -1, graphh, subtree_size)

    q = int(input())
    for _ in range(q):
        x = int(input())
        print(subtree_size[x])
