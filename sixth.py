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
    
    
    
    
    
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age cannot be 0 or less than")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
