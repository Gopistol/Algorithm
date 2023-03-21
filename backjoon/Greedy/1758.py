import sys


def input():
    return sys.stdin.readline().rstrip()

# tips 원소 - (index) => tip
n = int(input())
tips = []
tip = 0
for _ in range(n):
    tips.append(int(input()))
tips.sort(reverse=True)
for i in range(n):
    money = tips[i] - i
    if money > 0:
        tip += money
print(tip)
