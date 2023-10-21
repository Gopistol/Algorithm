def solution(triangle):
    n = len(triangle)
    a = [[0 for _ in range(i + 1)] for i in range(n)]

    answer = 0
    for i in range(n):
        for j in range(i + 1):
            if i == 0 and j == 0:
                a[i][j] = triangle[i][j]
            elif i > 0 and j == 0:
                a[i][j] = triangle[i][j] + a[i - 1][j]
            elif i > j > 0:
                a[i][j] = triangle[i][j] + max(a[i - 1][j],
                                               a[i - 1][j - 1])
            else:
                a[i][j] = triangle[i][j] + a[i - 1][j - 1]
            answer = max(answer, a[i][j])
    return answer