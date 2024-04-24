import sys
dwarfs = [int(sys.stdin.readline()) for _ in range(9)]
ex = sum(dwarfs) - 100
cont = False
for i in range(8):
    for j in range(i + 1, 9):
        t1 = dwarfs[i]
        t2 = dwarfs[j]
        if t1 + t2 == ex:
            dwarfs.remove(t1)
            dwarfs.remove(t2)
            cont = True
            break
    if cont:
        break
for dwarf in sorted(dwarfs):
    print(dwarf)