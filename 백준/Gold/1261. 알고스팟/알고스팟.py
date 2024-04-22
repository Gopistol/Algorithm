import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

maze = [list(map(int, input().rstrip())) for _ in range(m)]
crash = [[-1 for _ in range(n)] for _ in range(m)]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    crash[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]

            if n_x >= m or n_y >= n or n_x < 0 or n_y < 0:
                continue

            if crash[n_x][n_y] == -1:

                if maze[n_x][n_y]:  # 벽일 때
                    crash[n_x][n_y] = crash[x][y] + 1
                    queue.append((n_x, n_y))

                else:  # 빈 방일 때
                    crash[n_x][n_y] = crash[x][y]  # 부신 횟수 그대로 전달
                    queue.appendleft((n_x, n_y))  # 우선적으로 빈 방부터 돌기


bfs(0, 0)
print(crash[m - 1][n - 1])
