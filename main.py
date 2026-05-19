from src.utils import greet_user
from src.utils import average
from src.utils import is_palindrome

# 测试函数
print(average([1, 2, 3, 4]))
print(is_palindrome("level"))

# 用户输入
name = input("name: ")
age = input("age: ")

print(greet_user(name, age))