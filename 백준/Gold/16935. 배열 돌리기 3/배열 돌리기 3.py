import sys

input = sys.stdin.readline

n, m, c = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
r = list(map(int, input().split()))


def one(arr):  # 상하 반전
    return list(reversed(arr))


def two(arr):  # 좌우 반전
    return [list(reversed(row)) for row in arr]


def three(arr):  # 오른쪽 90도 회전
    return [list(col) for col in zip(*arr[::-1])]


def four(arr):  # 왼쪽 90도 회전
    return [list(row) for row in reversed(list(zip(*arr)))]


def five(arr):  # 사분면 시계방향 회전
    new_arr = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    mid_n = int(len(arr) / 2)
    mid_m = int(len(arr[0]) / 2)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i < mid_n:
                if j < mid_m:  # 1사분면
                    new_arr[i][j + mid_m] = arr[i][j]
                else:  # 2사분면
                    new_arr[i + mid_n][j] = arr[i][j]
            else:
                if j < mid_m:  # 4사분면 -> 1
                    new_arr[i - mid_n][j] = arr[i][j]
                else:  # 3사분면 -> 4
                    new_arr[i][j - mid_m] = arr[i][j]

    return new_arr


def six(arr):  # 사분면 반시계방향 회전
    new_arr = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    mid_n = int(len(arr) / 2)
    mid_m = int(len(arr[0]) / 2)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i < mid_n:
                if j < mid_m:  # 1사분면 -> 4
                    new_arr[i + mid_n][j] = arr[i][j]
                else:  # 2사분면 -> 1
                    new_arr[i][j - mid_m] = arr[i][j]
            else:
                if j < mid_m:  # 4사분면 -> 3
                    new_arr[i][j + mid_m] = arr[i][j]
                else:  # 3사분면 -> 2
                    new_arr[i - mid_n][j] = arr[i][j]

    return new_arr


for c in r:
    if c == 1:
        a = one(a)
    elif c == 2:
        a = two(a)
    elif c == 3:
        a = three(a)
    elif c == 4:
        a = four(a)
    elif c == 5:
        a = five(a)
    elif c == 6:
        a = six(a)

for i in range(len(a)):
    print(*a[i])
