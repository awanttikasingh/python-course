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




letters = ["a", "b", "c", "d"]

for index, letter in enumerate(letters):
    print(index, letter)

    
    
    
letters = ["a", "b", "c"]

# add
letters.append("d")
letters.insert(0, "-")
print(letters)


# remove
letters.pop(0)
letters.remove("b")
del letters[0:3]
# letters.clear()
print(letters)


print(letters.count("d"))
if "d" in letters:
    print(letters.index("d"))

    
    
    
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]


# def sort_item(item):
#    return item[1]


items.sort(key=lambda item: item[1])
print(items)


prices = list(map(lambda item: item[1], items))
print(prices)


filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
