n = int(input())
min_even = None
for i in range (1, n + 1):
    if i % 2 == 0:
        if min_even is None:
            min_even = i
if min_even is None:
    print("No")
else:
    print(min_even)

