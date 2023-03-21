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






def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizzbuzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"
    return input


print(fizz_buzz(15))




# task
def square(*numbers):
    for number in numbers:
        print(number * number, end=" ")


print(square(2, 5, 3, 7))
