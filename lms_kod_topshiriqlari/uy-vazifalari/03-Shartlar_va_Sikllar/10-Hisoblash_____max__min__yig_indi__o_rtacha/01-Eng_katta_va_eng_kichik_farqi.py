n = int(input())
first_num = int(input())
max_num = first_num
min_num = first_num
for _ in range(n - 1):
    num = int(input())
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print(max_num - min_num)

