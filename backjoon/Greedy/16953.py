import sys


def input():
    return sys.stdin.readline().rstrip()


a, b = map(int, input().split())
# b가 1로 끝나면 1 떼기
# b가 짝수면 2로 나누기
# 둘 다 아닐 경우 -1 출력
count = 1  # 연산 횟수
while a != b:
    if b % 2 == 0:
        b = int(b/2)
        count += 1
    elif b % 10 == 1 and b > 10:
        b = int(str(b)[:-1])  # 마지막 글자만 자르기
        count += 1
    else:
        count = -1
        break
print(count)
