import re
S=input()
k=input()
if not bool(re.search(k,S)):
    print((-1,-1))
else:
    l=0
    while bool(re.search(k,S)):
        m=re.search(k,S)
        print((m.start()+l,m.end()-1+l))
        S=S[m.start()+1:]
        l+=m.start()+1