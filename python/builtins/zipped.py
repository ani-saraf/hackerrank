a, b=input().split()
t=[]
for i in range(int(b)):
    x=map(float, input().split())
    t.append(x)
s = 0
a = zip(*t)
for i in a:
    for j in i:
        s+=j
    print(float(s)/int(b))
    s=0