import sys


def input():
    return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
coin = []
coin_count = 0
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
for i in range(n):
    if k >= coin[i]:
        coin_count += k // coin[i] # 꼭 1씩 증가시켜 줄 필요가 없었다! 시간 초과 이슈,,,
        k %= coin[i]
print(coin_count)
