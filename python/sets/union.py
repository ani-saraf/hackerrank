m = int(input())
a = set(list(map(int, input().split())))
n = int(input())
b = set(list(map(int, input().split())))
print(len(a.union(b)))
print(len(a.intersection(b)))
print(len(a.difference(b)))
print(len(b.difference(a)))
print(len(a.symmeteric_difference(b)))
