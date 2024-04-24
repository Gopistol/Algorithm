import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def rotate_layer(layer, r):
    total_elements = 2 * (n - 2 * layer) + 2 * (m - 2 * layer - 2)
    r = r % total_elements  # 실제로 회전해야 하는 횟수를 최소화
    elements = []

    # 현재 층의 요소를 순서대로 추출
    for i in range(layer, m - layer):
        elements.append(arr[layer][i])
    for i in range(layer + 1, n - layer):
        elements.append(arr[i][m - layer - 1])
    for i in range(m - layer - 2, layer - 1, -1):
        elements.append(arr[n - layer - 1][i])
    for i in range(n - layer - 2, layer, -1):
        elements.append(arr[i][layer])

    # 회전 처리
    rotated_elements = elements[r:] + elements[:r]

    # 회전된 요소 배치
    idx = 0
    for i in range(layer, m - layer):
        arr[layer][i] = rotated_elements[idx]
        idx += 1
    for i in range(layer + 1, n - layer):
        arr[i][m - layer - 1] = rotated_elements[idx]
        idx += 1
    for i in range(m - layer - 2, layer - 1, -1):
        arr[n - layer - 1][i] = rotated_elements[idx]
        idx += 1
    for i in range(n - layer - 2, layer, -1):
        arr[i][layer] = rotated_elements[idx]
        idx += 1


for layer in range(min(n, m) // 2):
    rotate_layer(layer, r)

for row in arr:
    print(*row)
