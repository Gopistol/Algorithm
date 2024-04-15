import sys

input = sys.stdin.readline

n = int(input())

li = [[] for _ in range(n + 1)]
visit = [[False for _ in range(n + 1)] for _ in range(n + 1)]


def bfs(i, j, visited):
    global apart_count
    if not visited[i][j] and li[i][j] == '1':
        apart_count += 1
        visited[i][j] = True
        # 좌, 우, 아래
        if i > 0:  # i가 맨 윗줄이 아닐 때만 위 탐색
            bfs(i - 1, j, visited)
        bfs(i, j + 1, visited)
        bfs(i, j - 1, visited)
        bfs(i + 1, j, visited)


for i in range(n):
    house = input().rstrip()
    li[i].extend(house)
    li[i].extend('0')  # 오른쪽 끝에 여분의 0 추가

li[len(li) - 1].extend('0' * (n + 1))  # 아래 여분의 0 한 줄 추가

apart_complex = []  # 단지 수

for i in range(n):
    for j in range(n):
        apart_count = 0
        bfs(i, j, visit)

        if apart_count:
            apart_complex.append(apart_count)

print(len(apart_complex))
apart_complex.sort()
for i in range(len(apart_complex)):
    print(apart_complex[i])
