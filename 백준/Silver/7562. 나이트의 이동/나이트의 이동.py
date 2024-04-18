import sys
from collections import deque

input = sys.stdin.readline

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(input())

def bfs(start, end, l):
    if start == end:
        return 0

    board = [[-1 for _ in range(l)] for _ in range(l)]

    queue = deque([start])
    board[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            n_x, n_y = x + dx[i], y + dy[i]

            if 0 <= n_x < l and 0 <= n_y < l and board[n_x][n_y] == -1:
                board[n_x][n_y] = board[x][y] + 1

                if (n_x, n_y) == end:
                    return board[n_x][n_y]

                queue.append((n_x, n_y))

    return board[end[0]][end[1]]


for _ in range(T):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    print(bfs(start, end, l))
