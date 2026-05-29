n = int(input())
if n < 2:

    print("No")
else:
    i = 2
    while True:
        if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)):
            print(i)
            break
        n += 1    
    
    
    
    
    
    
    