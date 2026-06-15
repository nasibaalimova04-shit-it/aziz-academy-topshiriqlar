n = int(input())
a = list(map(int,input().split()))
k = int(input())
ans = a[0]
for x in a:
    if abs(x - k) < abs(ans - k):
        ans = x
    elif abs(x - k) == abs(ans - k) and x < ans:
        ans = x
print(ans)        






