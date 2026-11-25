s = int(input())
c = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i + j == s:
            print(f"{i} + {j} = {s}")
            c += 1
print(f"Jami: {c}")            