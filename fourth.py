def greet():
    print("hi there")
    print("welcome aboard")


greet()




def greet(first_name, last_name):
    print(f"hi {first_name} {last_name}")
    print("welcome aboard")


greet("awanttika", "singh")




def get_greetings(name):
    return f"hi {name}"


message = get_greetings("avni")
print(message)




def increment(number, by):
    return number + by


print(increment(2, by=1))





def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


print(multiply(2, 5, 3, 7))





def save_user(**user):
    print(user)


save_user(id=1, name="avni", age=22)
