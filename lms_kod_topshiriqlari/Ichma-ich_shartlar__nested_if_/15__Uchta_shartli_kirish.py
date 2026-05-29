role, active = map(str,input().split())
if role == "admin":
    if int(active) == 1:
        print("Admin active")
    else:
        print("Admin inactive")
else:
        print("User")


