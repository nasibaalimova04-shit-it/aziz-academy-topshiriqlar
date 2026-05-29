user, age = map(str,input().split())

if user == "admin":
    if int(age) >= 18:    
        print("Full access")
    else:
         print("Limited")
else:
         print("No access")


