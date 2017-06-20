m = int(input())
a = set(map(int, input().split()))
for _ in range(int(input())):
    cmd, args = input().split(" ")
    b = set(map(int, input().split()))
    eval('a.'+cmd+'(b)')

print sum(A)

k,arr = int(input()),list(map(int, input().split()))

num = int(input)
lst = list(map(int, input().split())
s = set(lst)
print(((sum(s)*num)-(sum(lst)))//(num-1))