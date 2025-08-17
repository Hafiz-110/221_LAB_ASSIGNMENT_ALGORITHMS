import sys
sys.setrecursionlimit(2*10**6)
input = sys.stdin.readline

def dfs(r, c, grid, visited, R, H):
    # base cases (invalid cell)
    if r < 0 or r >= R or c < 0 or c >= H:
        return 0
    if visited[r][c] or grid[r][c] == '#':
        return 0

    visited[r][c] = True
    diamonds = 1 if grid[r][c] == 'D' else 0

    # explore 4 directions
    diamonds += dfs(r+1, c, grid, visited, R, H)
    diamonds += dfs(r-1, c, grid, visited, R, H)
    diamonds += dfs(r, c+1, grid, visited, R, H)
    diamonds += dfs(r, c-1, grid, visited, R, H)

    return diamonds

R, H = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
visited = [[False]*H for _ in range(R)]
max_diamonds = 0

for i in range(R):
    for j in range(H):
        if not visited[i][j] and grid[i][j] != '#':
            diamonds = dfs(i, j, grid, visited, R, H)
            max_diamonds = max(max_diamonds, diamonds)

print(max_diamonds)
