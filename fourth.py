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
