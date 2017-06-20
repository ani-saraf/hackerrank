m, n = map(int, input().split())
a = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
h = 0
for i in range(len(a)):
    if set([a[i]]).issubset(A):
        h +=1
    if set([a[i]]).issubset(B):
        h-=1

print(h)