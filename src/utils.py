def greet_user(name, age):
    return f"Hello {name}, you are {age} years old."


def average(nums):
    return sum(nums) / len(nums)


def is_palindrome(text):
    return text == text[::-1]

def answer_with_memory(name, age, history):
    if len(history) == 0:
        return f"Hello {name}, you are {age} years old."

    last = history[-1]

    return (
        f"Hello {name}, you are {age} years old.\n"
        f"(Memory: last input was '{last['input']}', last output was '{last['output']}')"
    )