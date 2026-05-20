import json
import os
from datetime import datetime


# ===== 自动定位项目根目录 =====
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data/log.json")


# ===== 创建统一 memory 结构 =====
def create_record(input_text, output_text, type="cli"):
    return {
        "timestamp": datetime.now().isoformat(),
        "input": input_text,
        "output": output_text,
        "type": type
    }


# ===== 写入 JSON memory（追加模式）=====
def append_record(record, path=DATA_PATH):

    os.makedirs(os.path.dirname(path), exist_ok=True)

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = []

    data.append(record)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# ===== 读取全部历史 =====
def load_history(path=DATA_PATH):

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []