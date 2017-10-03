n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
hcount=0
lcount=0
for i in range(1,n):
    if s[i] > max(s[0:i]):
        hcount+=1
    elif s[i] < min(s[0:i]):
        lcount+=1
print(hcount)
print(lcount)

=====================

def getRecord(s):
    for score in s:
        if len(h) == 0:
            h.append(score)
            l.append(score)
            next
        if score > max(h):
            h.append(score)
        if score < min(l):
            l.append(score)
    return len(h)-1, len(l)-1

h,l = [], []