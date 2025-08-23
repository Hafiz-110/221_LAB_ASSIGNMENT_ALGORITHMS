import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    n, m, s, d = map(int, input().split())

    def graph(n, m):
        g = [[] for _ in range(n+1)]
        for _ in range(m):
            u, v = map(int, input().split())
            g[u].append(v); g[v].append(u)
        return g
    g = graph(n, m)

    src = list(map(int, input().split()))
    des = list(map(int, input().split()))


    from collections import deque

    shortest = [-1]*(n+1)
    q = deque()

    for start in src:
        shortest[start] = 0
        q.append(start)

    while q:
        u = q.popleft()
        for v in g[u]:
            if shortest[v] == -1:
                shortest[v] = shortest[u] + 1
                q.append(v)

    print(' '.join(str(shortest[i]) for i in des))
