import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)


def dfs(start, graph, visited):
    to_visit = deque([start])

    while to_visit:
        node = to_visit.pop()
        if not visited[node]:
            visited[node] = True
            if node not in graph:
                return
            to_visit.extend(graph[node])


v_visited = [False for _ in range(N + 1)]
count = 0

for i in range(1, N + 1):
    if not v_visited[i]:
        dfs(i, graph, v_visited)
        count += 1

print(count)
