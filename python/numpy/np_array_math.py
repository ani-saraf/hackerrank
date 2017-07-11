import numpy as np
N, M = map(int,input().split())
A = np.array([input().split() for i in range(N)], dtype=int)
B = np.array([input().split() for j in range(N)], dtype=int)
print ( A+B, A-B, A*B, A//B, A%B, A**B, sep="\n" )