import sys

input = sys.stdin.readline
channel = 100  # 현재 채널

n = int(input())
m = int(input())

broken_buttons = list(map(int, input().split()))
min_count = abs(n - channel)

for number in range(10 ** 6 + 1):
    number = str(number)

    for j in range(len(number)):
        if int(number[j]) in broken_buttons:
            break
        elif j == len(number) - 1:
            min_count = min(min_count, len(number) + abs(int(number) - n))

print(min_count)
