import json
from datetime import datetime

# ===== 创建统一结构 =====
def create_record(input_text, output_text, type="cli"):
    return {
        "timestamp": datetime.now().isoformat(),
        "input": input_text,
        "output": output_text,
        "type": type
    }


# ===== 写入 JSON（追加 memory）=====
def append_record(path, record):

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = []

    data.append(record)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# ===== 读取全部历史 =====
def load_history(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []