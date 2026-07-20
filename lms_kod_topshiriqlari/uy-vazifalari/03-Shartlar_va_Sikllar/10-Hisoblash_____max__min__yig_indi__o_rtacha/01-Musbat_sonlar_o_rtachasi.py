n = int(input())
sum_pos = 0
count_pos = 0
for _ in range(n):
    num = int(input())
    if num > 0:
        sum_pos += num
        count_pos += 1
if count_pos > 0:
    print(sum_pos // count_pos)
else:
    print(0)







