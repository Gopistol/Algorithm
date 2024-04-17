import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(M)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(queue):
    day = 0
    while queue:
        x, y, day = queue.popleft()  # 현재 날짜 정보도 함께 추출
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and box[nx][ny] == 0:
                box[nx][ny] = 1
                queue.append((nx, ny, day + 1))  # 다음 날짜로 설정하여 추가
    return day


queue = deque()
for i in range(M):
    for j in range(N):
        if box[i][j] == 1:
            queue.append((i, j, 0))  # 초기 익은 토마토 위치와 날짜 0부터 시작

date = bfs(queue)

for row in box:
    if 0 in row:  # 익지 않은 토마토가 있으면 -1 출력
        print(-1)
        break
else:  # 모든 토마토가 익었으면 최종 날짜 출력
    print(date)
