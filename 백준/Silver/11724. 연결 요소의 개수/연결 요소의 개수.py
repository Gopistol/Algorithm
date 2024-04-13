import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = dict()

for _ in range(M):
    u, v = map(int, input().split())

    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u)

for key in graph:
    graph[key].sort()


def dfs(start, graph):
    visited = []
    to_visit = deque([start])

    while to_visit:
        node = to_visit.pop()

        if node not in visited:
            visited.append(node)
            if node not in graph:
                return
            to_visit.extend(graph[node])

    return visited


v_visited = [False for _ in range(N + 1)]
count = 0

for i in range(1, N + 1):

    if not v_visited[i]:
        vertexes = dfs(i, graph)
        if not vertexes:
            count += 1
            continue
        for v in vertexes:
            v_visited[v] = True

        count += 1

print(count)
