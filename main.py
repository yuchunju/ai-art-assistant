from src.storage import create_record, append_record, load_history
from src.csv_logger import append_csv
from src.utils import answer_with_memory
from src.api import predict_age

import os

print("CWD:", os.getcwd())

# =========================
# 1. 输入
# =========================
name = input("name: ")

# =========================
# 2. API（带异常处理）
# =========================
result = predict_age(name)

print("API result:", result)

age = result.get("age", 0)

# =========================
# 3. 读取 memory
# =========================
history = load_history()[-10:]

# =========================
# 4. 生成输出
# =========================
output = answer_with_memory(name, age, history)

print(output)

# =========================
# 5. 保存干净 output（关键）
# =========================
clean_output = output.split("\n")[0]

record = create_record(
    input_text=name,
    output_text=clean_output,
    type="cli"
)

append_record(record)

print("DEBUG: writing JSON...")

# =========================
# 6. 写 CSV
# =========================
append_csv(
    "data/results.csv",
    row=[name, age, clean_output],
    header=["name", "age", "output"]
)

print("DEBUG: writing CSV...")