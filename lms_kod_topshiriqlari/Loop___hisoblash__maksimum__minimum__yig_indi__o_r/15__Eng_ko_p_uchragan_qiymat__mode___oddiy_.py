n = int(input())
a = list(map(int,input().split()))
best_num = a[0]
best_count = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if a[j] == a[i]:
            cnt += 1
    if cnt > best_count:
        best_count = cnt
        best_num = a[i]
    elif cnt == best_count and a[i] < best_num:
        best_num = a[i]
print(best_num)




















