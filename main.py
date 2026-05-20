from src.storage import create_record, append_record, load_history
from src.csv_logger import append_csv
from src.utils import answer_with_memory
import os


print("CWD:", os.getcwd())


# =========================
# 1. 用户输入
# =========================
name = input("name: ")
age = input("age: ")


# =========================
# 2. 读取历史（JSON memory）
# =========================
history = load_history()


# =========================
# 3. AI 生成输出（带 memory）
# =========================
output = answer_with_memory(name, age, history)

print(output)


# =========================
# 4. 写入 JSON memory
# =========================
record = create_record(
    input_text=name,
    output_text=output,
    type="cli"
)

append_record(record)

print("DEBUG: writing JSON...")


# =========================
# 5. 写入 CSV log
# =========================
append_csv(
    "data/results.csv",
    row=[name, age, output.split("\n")[0]],
    header=["name", "age", "output"]
)

print("DEBUG: writing CSV...")