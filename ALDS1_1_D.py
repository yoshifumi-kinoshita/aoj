from sys import stdin


n = int(stdin.readline().rstrip())
Rmin = int(stdin.readline().rstrip())
maxv=-1000000000

for j in range(1,n):
    Rj = int(stdin.readline().rstrip())
    maxv=max((Rj-Rmin), maxv)
    Rmin=min(Rj, Rmin)

print(maxv)

