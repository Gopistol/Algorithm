import sys
from collections import deque

input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]

dice = [[0, 0, 0] for _ in range(4)]

t_y, t_x = (1, 1)
b_y, b_x = (3, 1)
u_y, u_x = (0, 1)
d_y, d_x = (2, 1)
l_y, l_x = (1, 0)
r_y, r_x = (1, 2)

n, m, y, x, k = map(int, input().split())

p = [list(map(int, input().split())) for _ in range(n)]
move = deque(map(int, input().split()))


def flip(direction):
    global dice

    t = dice[t_y][t_x]
    b = dice[b_y][b_x]
    l = dice[l_y][l_x]
    r = dice[r_y][r_x]
    u = dice[u_y][u_x]
    d = dice[d_y][d_x]

    if direction == 1:
        # up, down은 안바뀜 4 1 3 / 6 -> 6 4 1 / 3
        dice[l_y][l_x] = b
        dice[t_y][t_x] = l
        dice[r_y][r_x] = t
        dice[b_y][b_x] = r
    # 서쪽
    elif direction == 2:
        # up, down은 안바뀜 4 1 3 / 6 -> 1 3 6 / 4
        dice[l_y][l_x] = t
        dice[t_y][t_x] = r
        dice[r_y][r_x] = b
        dice[b_y][b_x] = l
        # 북쪽
    elif direction == 3:
        # l, r은 안바뀜 2 1 5 6 -> 1 5 6 2
        dice[u_y][u_x] = t
        dice[t_y][t_x] = d
        dice[b_y][b_x] = u
        dice[d_y][d_x] = b
    # 남쪽
    elif direction == 4:
        # l, r은 안바뀜 2 1 5 6 -> 6 2 1 5
        dice[u_y][u_x] = b
        dice[t_y][t_x] = u
        dice[b_y][b_x] = d
        dice[d_y][d_x] = t


while move:
    d = move.popleft()
    dx, dy = direction[d - 1]
    nx, ny = x + dx, y + dy

    if nx < 0 or nx >= m or ny < 0 or ny >= n:
        continue

    flip(d)
    if p[ny][nx] == 0:
        p[ny][nx] = dice[b_y][b_x]
    else:
        dice[b_y][b_x] = p[ny][nx]
        p[ny][nx] = 0

    print(dice[t_y][t_x])
    (x, y) = (nx, ny)
