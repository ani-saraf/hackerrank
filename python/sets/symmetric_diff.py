m = int(input())
a = set(list(map(int, input().split())))
n = int(input())
b = set(list(map(int, input().split())))
c =  list(a.difference(b)) + list(b.difference(a))
c.sort()
for i in c:
    print(i)
