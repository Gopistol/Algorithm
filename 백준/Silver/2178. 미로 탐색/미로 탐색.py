import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

maze = [list(map(int, input().rstrip())) for _ in range(N)]

# 아래, 오른쪽, 왼쪽, 위쪽 방향 벡터
dx = [0, 1, -1, 0]
dy = [-1, 0, 0, 1]


def dfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]

            if n_x < 0 or n_x >= N or n_y < 0 or n_y >= M:
                continue

            if maze[n_x][n_y] == 0:
                continue

            if maze[n_x][n_y] == 1:
                maze[n_x][n_y] = maze[x][y] + 1
                queue.append((n_x, n_y))

    return maze[N - 1][M - 1]


print(dfs(0, 0))
