n = int(input())

y = 0
while n > 0:
    r = n % 10
    y += r 
    n = n // 10
print(y)

