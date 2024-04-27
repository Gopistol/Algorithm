import sys

input = sys.stdin.readline

n = int(input())
board = [list(input()) for _ in range(n)]


def find_candy():
    global board
    max_count = 1
    # 가로 확인
    for i in range(n):
        c_count = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                c_count += 1
            else:
                c_count = 1
            max_count = max(max_count, c_count)

    # 세로
    for i in range(n):
        l_count = 1
        for j in range(1, n):
            if board[j][i] == board[j - 1][i]:
                l_count += 1
            else:
                l_count = 1
            max_count = max(max_count, l_count)

    return max_count


def switch(prev, next):
    global board
    py, px = prev
    ny, nx = next

    board[py][px], board[ny][nx] = board[ny][nx], board[py][px]


answer = 1

for i in range(n):
    for j in range(n - 1):
        if j + 1 < n and board[i][j] != board[i][j + 1]:
            switch((i, j), (i, j + 1))
            answer = max(answer, find_candy())
            switch((i, j + 1), (i, j))

        if i + 1 < n and board[i][j] != board[i + 1][j]:
            switch((i, j), (i + 1, j))
            answer = max(answer, find_candy())
            switch((i + 1, j), (i, j))

print(answer)
