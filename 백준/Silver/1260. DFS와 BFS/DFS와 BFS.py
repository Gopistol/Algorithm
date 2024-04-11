import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = dict()

for _ in range(M):
    A, B = map(int, input().split())
    if A not in graph:
        graph[A] = []
    if B not in graph:
        graph[B] = []

    graph[A].append(B)
    graph[B].append(A)


def dfs(graph, start):
    visited = []
    to_visit = deque([start])

    while to_visit:
        node = to_visit.pop()
        if node not in visited:
            print(node, end=' ')
            visited.append(node)
            if node not in graph:
                return
            to_visit.extend(graph[node])


def bfs(graph, start):
    visited = []
    to_visit = deque([start])

    while to_visit:
        node = to_visit.popleft()
        if node not in visited:
            visited.append(node)
            print(node, end=' ')

            if node not in graph:
                return
            to_visit.extend(graph[node])


for key in graph:
    graph[key].sort(reverse=True)  # key 내림차순 정렬
dfs(graph, V)

print()

for key in graph:
    graph[key].sort()  # key 오름차순 정렬
bfs(graph, V)
