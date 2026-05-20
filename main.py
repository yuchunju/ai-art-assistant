from src.storage import create_record, append_record, load_history
from src.utils import answer_with_memory

name = input("name: ")
age = input("age: ")

# 1. 读取历史
history = load_history("data/log.json")

# 2. 生成回答（带 memory）
output = answer_with_memory(name, age, history)

print(output)

# 3. 写入新记录
record = create_record(name, output, type="cli")
append_record("data/log.json", record)