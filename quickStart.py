import torch

# """ Python is working! """
print("Python is working!")

# Python 3: List comprehensions
fruits = ["apple", "banana", "cherry"]
loud_fruits = [fruit.upper() for fruit in fruits]
print(loud_fruits)

# List and the enumerate function
list(enumerate(fruits))
print(list(enumerate(fruits)))


x = torch.rand(2, 3)
print(x)