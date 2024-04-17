import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(M)]
date = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 아래, 위, 우, 좌


def bfs(x, y):  # 1인 토마토들만 Dfs실행
    queue = deque()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue

        if box[nx][ny] == -1:
            continue

        if box[nx][ny] == 0:
            box[nx][ny] = 1
            queue.append((nx, ny))

    if queue:
        return queue
    else:
        return 0


def ripe_per_day(queue):
    l = len(queue)
    next_ripe = deque()
    for _ in range(l):
        x, y = queue.popleft()
        q = bfs(x, y)
        while q:
            next_ripe.append(q.popleft())

    return next_ripe


def all_riped():
    count = 0
    for idx in range(M):
        count += box[idx].count(0)
    return count


# 1인 인덱스 모두 탐색
# 걔네들만 한번에 bfs돌리기
# 돌릴때마다 0이 남아있는지 체크
# date가 N * M을 넘었는데도 0이 남아있으면 -1로 판정

ripe = deque()

for i in range(M):
    for j in range(N):
        if box[i][j] == 1:
            ripe.append((i, j))

date = 0

while True:
    ripe = ripe_per_day(ripe)
    
    if not ripe:  # 다음에 익을 토마토가 없을 때,
        if not all_riped():  # 모두 다 익었으면 탈출
            break
        else:  # 남아있으면 모두 익는 건 불가능하다고 판단
            date = -1
            break

    date += 1


print(date)
