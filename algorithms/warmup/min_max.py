arr = sorted(list(map(int, input().split())))
print(sum(arr[:4]), sum(arr[1:]))
#===============

lst = list(map(int, input().split()))
x = sum(lst)
print((x-(max(lst))), (x-(min(lst))))