n = int(input())
max_num = int(input())
max_pos = 1
for i in range(2, n + 1):
    num = int(input())
    if num > max_num:
        max_num = num
        max_pos = i
print(max_pos)