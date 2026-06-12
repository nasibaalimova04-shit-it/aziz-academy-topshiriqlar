n = int(input())
a = list(map(int,input().split()))
mn = a[0]
for i in range(1, n):
    if a[i] < mn:
        mn = a[i]
print(mn)

