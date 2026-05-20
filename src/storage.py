from datetime import datetime
import json

# 定义“记录结构生成函数”
def create_record(input_text, output_text, type="cli"):
    return {
        "timestamp": datetime.now().isoformat(),
        "input": input_text,
        "output": output_text,
        "type": type
    }

# JSON读取
def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []
    
# JSON写入
def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# 追加记录到JSON文件
def append_record(path, record):
    data = load_json(path)
    data.append(record)
    save_json(path, data)    

    