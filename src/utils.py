def answer_with_memory(name, age, history):
    base = f"Hello {name}, you are {age} years old."

    if not history:
        return base

    last = history[-1]

    # ❗关键：防止递归嵌套 memory
    last_input = last.get("input", "")
    last_output = last.get("output", "")

    # ❗只截断，不允许继续拼 memory
    return (
        base + "\n"
        + f"(Memory: last input was '{last_input}', last output was '{last_output}')"
    )