import sys

dwarfs = [int(sys.stdin.readline()) for _ in range(9)]
ex = sum(dwarfs) - 100


def find():
    global dwarfs
    for i in range(9):
        for j in range(9):
            if i == j:
                continue
            if ex == dwarfs[i] + dwarfs[j]:
                return dwarfs[i], dwarfs[j]


ex_1, ex_2 = find()
dwarfs.remove(ex_1)
dwarfs.remove(ex_2)
for dwarf in sorted(dwarfs):
    print(dwarf)
