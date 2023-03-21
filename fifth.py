numbers = list(range(20))
print(numbers)


chars = list("hello world")
print(chars)


numbers = list(range(20))
print(numbers[::2])




numbers = [2, 5, 6, 18, 5, 2, 6, 5, 2, 3]
first, *others, last = numbers
print(first, last)
print(others)
