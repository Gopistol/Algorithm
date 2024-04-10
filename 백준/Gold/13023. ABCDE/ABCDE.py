import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)  # 재귀 호출 시 설정해야 함

N, M = map(int, input().split())

visited = [False for _ in range(2001)]  # 문제 조건: N = 2000
relation = [[] for _ in range(N)]
answer = 0

for i in range(M):  # 친구 관계 설정
    A, B = map(int, input().split())
    relation[A].append(B)
    relation[B].append(A)


def dfs(index, count):
    global answer

    if count == 4:  # 친구 관계가 4번 이상 엮여 있으면 True 반환
        answer = 1
        print(answer)
        sys.exit()

    visited[index] = True

    for idx in relation[index]:
        if not visited[idx]:
            dfs(idx, count + 1)

    visited[index] = False


for i in range(N):
    dfs(i, 0)
    visited[i] = False

print(answer)
