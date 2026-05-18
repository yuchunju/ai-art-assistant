print("hello world")

name = input("name: ")
age = input("age: ")
print(f"Hello {name}, you are {age}")

foods = ["pizza", "tea", "rice"]
for food in foods:
    print(food)

person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(f"{key}: {value}")
    