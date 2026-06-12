n = int(input())
a = list(map(int,input().split()))
mx = a[0]
idx = 0
for i in range(1, n):
    if a[i] > mx:
        mx = a[i]
        idx = i
print(idx)        










