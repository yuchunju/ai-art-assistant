import csv
import os


# ===== 自动定位项目根目录 =====
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# ===== CSV 写入（追加日志）=====
def append_csv(filename, row, header=None):

    path = os.path.join(BASE_DIR, filename)

    file_exists = os.path.exists(path)

    # 如果文件不存在，自动创建目录
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # 写表头（只写一次）
        if not file_exists and header:
            writer.writerow(header)

        writer.writerow(row)