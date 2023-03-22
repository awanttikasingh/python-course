try:
    age = int(input("age:"))
except ValueError as ex:
    print("you didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("no exceptions thrown")
print("execution continues")





try:
    age = int(input("age:"))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age.")

else:
    print("no exceptions thrown")

    
    
    
    
    
    try:
    file = open("sixth.py")
    age = int(input("age:"))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age.")

else:
    print("no exceptions thrown")
finally:
    file.close()
