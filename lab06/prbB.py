import sys
input = sys.stdin.readline

def graph(n, m):
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    return g

n, m = map(int, input().split())
g = graph(n, m)


from collections import deque

def bipartite(g, n):
    color = {i:-1 for i in range(1, n+1)}
    res = 0

    for start in range(1, n+1):
        if color[start] == -1:
            q = deque([start])
            color[start] = 0
            count = [1, 0]    # count[0] = zeros, count[1] = ones
            while q:
                u = q.popleft()
                for v in g[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        count[color[v]] += 1
                        q.append(v)

            res += max(count)
    
    print(res)

bipartite(g, n)

