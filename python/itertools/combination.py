from itertools import combinations
S, k = input().split()
S = sorted(S)
k = int(k)
for j in range(1, k+1):
    print(*(''.join(i) for i in combinations(S, j)), sep="\n")