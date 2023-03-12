import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip('\n').split())
array = list(map(int, input().rstrip('\n').split()))
min_diff = m
min_diff_sum = 0
for i in range(len(array)):
    for j in range(len(array)):
        for k in range(len(array)):
            if i != j and j != k and k != i:
                diff = m - (array[i] + array[j] + array[k])
                if min_diff >= diff >= 0:
                    min_diff = diff
                    min_diff_sum = array[i] + array[j] + array[k]

print(min_diff_sum)
