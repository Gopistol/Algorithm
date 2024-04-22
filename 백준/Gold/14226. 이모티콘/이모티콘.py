import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
d = [[-1] * (t + 1) for _ in range(t + 1)]

q = deque()
q.append((1, 0))

d[1][0] = 0  # 시간 초기화

while q:
    s, c = q.popleft()  # 스크린, 클립보드의 이모수콘 개수
    # 복사 (s, c) -> (s, s)
    if d[s][s] == -1:
        d[s][s] = d[s][c] + 1
        q.append((s, s))
    # 붙여넣기 (s, c) -> (s + c, c)
    if s + c <= t and d[s + c][c] == -1:
        d[s + c][c] = d[s][c] + 1
        q.append((s + c, c))
    # 삭제 (s, c) -> (s - 1, c)
    if s - 1 >= 0 and d[s - 1][c] == -1:
        d[s - 1][c] = d[s][c] + 1
        q.append((s - 1, c))

a = list(d[t])
a.remove(-1)  # 방문하지 않은 곳의 기본값 제거
print(min(a))
