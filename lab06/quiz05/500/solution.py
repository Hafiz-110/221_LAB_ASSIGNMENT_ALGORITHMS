import sys
from collections import deque
input = sys.stdin.readline

moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

t = int(input())
for _ in range(t):
    N, K, X, Y = map(int,input().split())
    vis = [[ -1 for _ in range(N+1)] for _ in range(N+1)]
    q = deque()
    q.append((X,Y,0))
    vis[X][Y] = 0
    while q:
        x, y, d = q.popleft()
        if d==K: continue
        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 1<=nx<=N and 1<=ny<=N and vis[nx][ny] == -1:
                vis[nx][ny] = d+1
                q.append((nx, ny, d+1))
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if vis[i][j] != -1 and vis[i][j] <= K:
                ans += 1
    print(ans)
