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


#list comprehensions/filter/map
# prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]
print(prices)


# filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
print(filtered)




#zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip("abd", list1, list2)))



#stacks
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])





#queues
from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")

    
    
    
# tupple
point = (1, 2, 3)
print(point[0:2])



# swapping
x = 10
y = 11

x, y = y, x

print("x", x)
print("y", y)




# array
from array import array

numbers = array("i", [1, 2, 3])
numbers.append(6)
print(numbers)



# sets
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

if 1 in first:
    print("yes")
