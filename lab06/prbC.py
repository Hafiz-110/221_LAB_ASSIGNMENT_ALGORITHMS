import sys 
from collections import deque 
  
input = sys.stdin.readline 
  
N = int(input()) 
x1, y1, x2, y2 = map(int, input().split()) 
  
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), 
         (1, 2), (1, -2), (-1, 2), (-1, -2)] 
  
dist = [[-1] * (N + 1) for _ in range(N + 1)] 
dist[x1][y1] = 0 
q = deque([(x1, y1)]) 
  
while q: 
    x, y = q.popleft() 
    if (x, y) == (x2, y2): 
        print(dist[x][y]) 
        exit() 
  
    for dx, dy in moves: 
        nx, ny = x + dx, y + dy 
        if 1 <= nx <= N and 1 <= ny <= N and dist[nx][ny] == -1: 
            dist[nx][ny] = dist[x][y] + 1 
            q.append((nx, ny)) 
  
print(-1)

