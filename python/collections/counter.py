from collections import Counter
X = int(input())
shoe_size_all = Counter(map(int, input().split()))
price_list=[]
for i in range(int(input())):
    cust_size, cust_price = map(int, input().split())
    if shoe_size_all[cust_size] > 0:
        price_list.append(cust_price)
        shoe_size_all.subtract(Counter([cust_size]))
print(sum(price_list))