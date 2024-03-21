import sys

input = sys.stdin.readline


def append_star(len):
    if len == 1:
        return ["*"]

    k = len // 3
    stars = append_star(k)
    l = []

    for s in stars:
        l.append(s * 3)
    for s in stars:
        l.append(s + " " * k + s)
    for s in stars:
        l.append(s * 3)

    return l


n = int(input())
print("\n".join(append_star(n)))
