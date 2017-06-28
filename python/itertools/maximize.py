from itertools import product
K, M = input().split()
squared_lst = []
array_num = []

for i in range(int(K)):
    array_num.append([int(x)*int(x) for x in input().split()][1:]) #creates list of squares
combn = list(product(*array_num))
for val in combn:
    result = sum(val)%int(M)  # creates list of sum of squares
    squared_lst.append(result)
print(squared_lst)
print(max(squared_lst))