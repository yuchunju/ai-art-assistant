# 读取历史
from src.storage import create_record, append_record, load_json
from src.utils import greet_user

history = load_json("data/log.json")

# 让 AI “看历史”
print("\n=== MEMORY CONTEXT ===")
for item in history[-3:]:
    print(item["input"], "→", item["output"])

# 把历史“喂给当前输出逻辑”
name = input("name: ")
age = input("age: ")

# 用历史做一个简单增强
if history:
    last = history[-1]["output"]
    print("\n(last memory):", last)

output = greet_user(name, age)

print(output)

# 继续写入 memory（闭环）
record = create_record(
    input_text=name,
    output_text=output,
    type="cli-memory"
)

append_record("data/log.json", record)