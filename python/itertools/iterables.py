from itertools import combinations

n = int(input())
k = input().split()
l = int(input())
count = 0

lst = list(combinations(k, l))
lst_len = float(len(lst))

for i in lst:
    if 'a' in i:
        count += 1

print(float(count) / lst_len)