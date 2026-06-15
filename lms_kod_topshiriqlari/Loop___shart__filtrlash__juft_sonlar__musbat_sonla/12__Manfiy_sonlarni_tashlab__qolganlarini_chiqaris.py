n = int(input())
sonlar = list(map(int,input().split()))
for x in sonlar:
    if x < 0:
        continue
    print(x)


