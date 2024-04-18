import sys
from collections import deque

input = sys.stdin.readline

# 방향 8개
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(input())


# board의 각 칸마다 나이트가 몇 번을 이동해야 올 수 있는지
# 최소 count를 저장


def bfs(start, end, board):
    queue = deque([start])
    e_i, e_j = end

    if start == end:
        return 0

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            n_x = x + dx[i]
            n_y = y + dy[i]

            if n_x < 0 or n_x >= len(board) or n_y < 0 or n_y >= len(board):
                continue

            if board[n_x][n_y] > 0:
                continue

            if n_x == e_i and n_y == e_j:
                board[n_x][n_y] = board[x][y] + 1
                break

            board[n_x][n_y] = board[x][y] + 1
            queue.append((n_x, n_y))

    return board[e_i][e_j]


for _ in range(T):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    board = [[0 for _ in range(l)] for _ in range(l)]

    print(bfs(start, end, board))
 