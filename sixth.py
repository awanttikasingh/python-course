try:
    age = int(input("age:"))
except ValueError as ex:
    print("you didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("no exceptions thrown")
print("execution continues")
