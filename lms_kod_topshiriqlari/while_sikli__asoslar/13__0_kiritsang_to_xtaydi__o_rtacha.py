yigindi = 0
son = 0
while True:
    n = int(input())
    if n == 0:
        break
    yigindi += n    
    son += 1
if son == 0:
    print(0)
else:    
    print(yigindi/son)






