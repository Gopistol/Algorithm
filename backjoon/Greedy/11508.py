import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
stock = []
payment = 0
for _ in range(n):
    stock.append(int(input()))
stock.sort(reverse=True)
for i in range(n):
    if (i + 1) % 3 != 0:
        payment += stock[i]
print(payment)
